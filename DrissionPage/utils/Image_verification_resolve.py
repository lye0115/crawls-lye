import cv2
import os 

def find_gap(bg_img:str, slider_img:str):
        """用 OpenCV 寻找缺口位置"""
        # 转为灰度图
        bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        slider_gray = cv2.cvtColor(slider_img, cv2.COLOR_BGR2GRAY)

        # 边缘检测
        bg_edge = cv2.Canny(bg_gray, 50, 150)
        slider_edge = cv2.Canny(slider_gray, 50, 150)

        # 模板匹配
        result = cv2.matchTemplate(bg_edge, slider_edge, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 缺口左上角坐标
        top_left = max_loc
        # 计算缺口中心 x 坐标（滑块需要移动的距离）
        gap_x = top_left[0] + slider_img.shape[1] // 2
        return gap_x


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    bg_img = cv2.imread('images/bg-img.png')
    slider_img = cv2.imread('images/slider_img.png')
    
    # 检查图片是否成功加载
    if bg_img is None:
        print("错误：无法加载背景图片 images/bg-img.png")
        exit(1)
    if slider_img is None:
        print("错误：无法加载滑块图片 images/slider_img.png")
        exit(1)
    
    gap_x = find_gap(bg_img, slider_img)
    print(gap_x)