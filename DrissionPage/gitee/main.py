import time
from DrissionPage import Chromium,ChromiumOptions
import requests
# from ..utils.Image_verification_resolve import find_gap
import cv2
import os 
import random
import numpy as np

co = ChromiumOptions().auto_port()

os.chdir(os.path.dirname(__file__))

def find_gap(bg_img_path: str, slider_img_path: str):
    """用 OpenCV 寻找滑动验证码的缺口位置"""
    bg_img = cv2.imread(bg_img_path)
    slider_img = cv2.imread(slider_img_path)
    
    if bg_img is None or slider_img is None:
        print("图像读取失败")
        return 0
    
    print(f"背景图尺寸: {bg_img.shape}")
    print(f"滑块图尺寸: {slider_img.shape}")
    
    # 第一步：从滑块图片中提取实际的拼图部分
    puzzle_piece = extract_puzzle_piece(slider_img)
    
    if puzzle_piece is None:
        print("无法提取拼图块")
        return 0
    
    print(f"提取的拼图块尺寸: {puzzle_piece.shape}")
    
    # 第二步：在背景图中寻找匹配的缺口位置
    gap_x = find_gap_position(bg_img, puzzle_piece)
    
    print(f"检测到缺口位置: x={gap_x}")
    return gap_x

def extract_puzzle_piece(slider_img):
    """从滑块图片中提取实际的拼图部分"""
    # 转为灰度图
    gray = cv2.cvtColor(slider_img, cv2.COLOR_BGR2GRAY)
    
    # 使用阈值分割，分离前景和背景
    # 通常拼图部分颜色较深，背景较浅
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 形态学操作，去除噪点
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)
    
    # 寻找轮廓
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print("未找到拼图轮廓")
        return None
    
    # 找到最大的轮廓（假设是拼图）
    max_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(max_contour)
    
    print(f"拼图轮廓面积: {area}")
    
    # 如果面积太小，可能不是拼图
    if area < 100:
        print("拼图面积过小")
        return None
    
    # 获取拼图的边界矩形
    x, y, w, h = cv2.boundingRect(max_contour)
    print(f"拼图边界: x={x}, y={y}, w={w}, h={h}")
    
    # 创建mask
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.fillPoly(mask, [max_contour], 255)
    
    # 提取拼图区域（带mask）
    puzzle_region = gray[y:y+h, x:x+w]
    puzzle_mask = mask[y:y+h, x:x+w]
    
    # 将背景设为白色，拼图保持原色
    puzzle_piece = np.where(puzzle_mask == 255, puzzle_region, 255)
    
    return puzzle_piece

def find_gap_position(bg_img, puzzle_piece):
    """在背景图中寻找与拼图匹配的缺口位置"""
    # 转为灰度图
    bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    
    # 对拼图进行边缘检测
    puzzle_edges = cv2.Canny(puzzle_piece, 50, 150)
    
    # 对背景进行边缘检测
    bg_edges = cv2.Canny(bg_gray, 50, 150)
    
    # 使用模板匹配
    result = cv2.matchTemplate(bg_edges, puzzle_edges, cv2.TM_CCOEFF_NORMED)
    
    # 寻找最佳匹配位置
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    print(f"模板匹配度: {max_val:.4f}")
    
    # 如果匹配度过低，尝试其他方法
    if max_val < 0.3:
        print("匹配度较低，尝试反向匹配")
        # 尝试反向匹配（寻找缺口而不是凸起）
        inverted_puzzle = 255 - puzzle_edges
        result = cv2.matchTemplate(bg_edges, inverted_puzzle, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        print(f"反向匹配度: {max_val:.4f}")
    
    # 如果还是不好，使用轮廓匹配
    if max_val < 0.3:
        print("使用轮廓匹配方法")
        return find_gap_by_contour_matching(bg_gray, puzzle_piece)
    
    gap_x = max_loc[0]
    return gap_x

def find_gap_by_contour_matching(bg_gray, puzzle_piece):
    """通过轮廓匹配寻找缺口位置"""
    # 寻找背景图中的所有轮廓
    bg_edges = cv2.Canny(bg_gray, 50, 150)
    bg_contours, _ = cv2.findContours(bg_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 寻找拼图的轮廓
    puzzle_edges = cv2.Canny(puzzle_piece, 50, 150)
    puzzle_contours, _ = cv2.findContours(puzzle_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not puzzle_contours or not bg_contours:
        print("轮廓匹配失败，使用默认位置")
        return int(bg_gray.shape[1] * 0.3)  # 默认位置
    
    # 获取拼图主轮廓
    puzzle_contour = max(puzzle_contours, key=cv2.contourArea)
    
    best_match_x = 0
    best_similarity = 0
    
    # 在背景图中滑动匹配
    puzzle_h, puzzle_w = puzzle_piece.shape
    
    for x in range(0, bg_gray.shape[1] - puzzle_w, 5):  # 每5像素检查一次
        # 提取背景区域
        bg_region = bg_gray[0:puzzle_h, x:x+puzzle_w]
        bg_region_edges = cv2.Canny(bg_region, 50, 150)
        
        # 计算相似度（简单的像素匹配）
        similarity = cv2.matchTemplate(bg_region_edges, puzzle_edges, cv2.TM_CCOEFF_NORMED)
        max_sim = np.max(similarity)
        
        if max_sim > best_similarity:
            best_similarity = max_sim
            best_match_x = x
    
    print(f"轮廓匹配最佳相似度: {best_similarity:.4f}, 位置: x={best_match_x}")
    
    return best_match_x


def main():
    # 创建浏览器对象
    browser = Chromium(co)
    # 创建标签页
    tab = browser.latest_tab
    # 访问网页
    tab.get('https://gitee.com/login')
    # 定位到账号文本框，获取文本框元素
    ele = tab.ele('#user_login').input('lishuai')
    # 定位到密码文本框并输入密码
    tab.ele('#user_password').input('L3244886+')
    # 点击登录按钮
    tab.ele('@value=登 录').click()
    # 等待3秒看是否出现滑块验证
    slider_ele = tab.ele('.yp-riddler-slide-img-container', timeout=3)
    if(slider_ele):
        # 背景图
        bg_img_url = tab.ele('.yp-riddler-slider-bg').attr('src')
        # 验证块 yp-riddler-slider-front
        slider_img = tab.ele('.yp-riddler-slider-front')
        slider_img_url = slider_img.attr('src')
        # 下载到本地
        time_stamp = int(time.time() * 1000)
        try:
          os.mkdir(str(time_stamp))
          os.makedirs(str(time_stamp), exist_ok=True)
          with open(f'{time_stamp}/bg-img.png', 'wb') as f:

            f.write(requests.get(bg_img_url).content)
          with open(f'{time_stamp}/slider-img.png', 'wb') as f:
            f.write(requests.get(slider_img_url).content)
          gap =  find_gap(f'{time_stamp}/bg-img.png', f'{time_stamp}/slider-img.png')
          print(gap)
        except Exception as e:
            browser.quit()
            print(f'错误：{e}')   
        
        # 如果成功获取到缺口位置，开始模拟滑动
        if 'gap' in locals():
            # 获取滑动按钮和背景图的实际尺寸
            slider_button = tab.ele('.yp-riddler-slider-front')  # 实际的滑动按钮
            
            # 获取背景图在网页中的实际尺寸
            bg_web_width = tab.run_js('return document.querySelector(".yp-riddler-slider-bg").offsetWidth;')

            # 获取下载图片的实际尺寸
            bg_downloaded = cv2.imread(f'{time_stamp}/bg-img.png')
            bg_img_width = bg_downloaded.shape[1]  # 下载图片的宽度
            
            # 计算缩放比例
            scale_ratio = bg_web_width / bg_img_width
            print(f"网页宽度: {bg_web_width}, 图片宽度: {bg_img_width}, 缩放比例: {scale_ratio:.3f}")
            
            # 将图像坐标转换为网页坐标
            actual_gap_position = gap * scale_ratio
            
            # 获取滑块按钮当前位置

            slider_current_x = tab.run_js('''
                        var slider = document.querySelector(".yp-riddler-slider-front");
                        var bg = document.querySelector(".yp-riddler-slider-bg");
                        return slider.offsetLeft - bg.offsetLeft;
                    ''')
            
            # 计算实际需要移动的距离
            move_distance = actual_gap_position - slider_current_x
            
            print(f"图像中检测到的缺口位置: {gap}")
            print(f"网页中的实际缺口位置: {actual_gap_position:.1f}")
            print(f"滑块当前位置: {slider_current_x}")
            print(f"需要移动距离: {move_distance:.1f}")
            
            # 如果移动距离太小，可能检测有误
            if abs(move_distance) < 10:
                print("移动距离过小，可能检测有误")
                move_distance = bg_web_width * 0.3  # 使用估算距离
            
            # 模拟人工滑动
            actions = tab.actions
            # 移动到滑块中心
            actions.move_to(slider_button)
            # 按下鼠标
            actions.hold()
            
            # 分段移动，模拟真实滑动
            total_distance = move_distance - 2   # 减去一些距离防止过度
            steps = random.randint(3,5)  # 增加步数，更像人工
            
            for i in range(steps):
                # 计算每步移动距离
                if i < steps * 0.7:  # 前70%快速移动
                    step_distance = total_distance * 0.8 / (steps * 0.7)
                else:  # 后30%慢速调整
                    step_distance = total_distance * 0.2 / (steps * 0.3)
                
                # 添加随机抖动
                jitter_x = random.uniform(-1, 1)
                jitter_y = random.uniform(-0.5, 0.5)
                
                # 移动
                actions.move(step_distance + jitter_x, jitter_y)
                
                # 随机延迟
                time.sleep(random.uniform(0.01, 0.03))
            
            # 释放鼠标
            actions.release()
            # 执行动作链
            # actions.perform()
            
            time.sleep(2)  # 等待验证结果
            
            print('滑动完成')
            
if __name__ == '__main__':
    main()