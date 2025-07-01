import asyncio
import json
import time
import pandas as pd
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

# 全局共享的浏览器配置
SHARED_BROWSER_CONFIG = BrowserConfig(
    headless=False,  # 可以设置为True以节省资源
    verbose=True,
    user_agent_mode='random',
    extra_args=["--no-first-run", "--disable-blink-features=AutomationControlled"]
)

def load_config():
    """加载配置文件"""
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_browser_config_for_thread(thread_id=None):
    """
    为线程获取浏览器配置
    使用共享配置，但确保线程安全
    """
    # 直接返回共享配置
    # crawl4ai内部会处理多线程安全问题
    return SHARED_BROWSER_CONFIG

def run_single_account_task(account_info, config):
    """
    在单个线程中运行单个账户的任务
    """
    thread_id = threading.current_thread().ident
    print(f"[线程 {thread_id}] 开始处理账户: {account_info['username']}")
    
    # 创建新的事件循环（每个线程需要独立的事件循环）
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # 使用共享的浏览器配置
        browser_config = get_browser_config_for_thread(thread_id)
        
        # 调用原有的异步函数
        result = loop.run_until_complete(
            auto_login_and_extract_with_shared_config(
                url=config['target_url'],
                username=account_info['username'],
                password=account_info['password'],
                page_size=config['page_size'],
                page_count=config['page_count'],
                browser_config=browser_config,
                thread_id=thread_id
            )
        )
        
        if result:
            print(f"[线程 {thread_id}] 账户 {account_info['username']} 处理完成，获取 {len(result.get('all_page_data', []))} 条数据")
            return {
                'account': account_info['username'],
                'status': 'success',
                'data': result,
                'thread_id': thread_id
            }
        else:
            print(f"[线程 {thread_id}] 账户 {account_info['username']} 处理失败")
            return {
                'account': account_info['username'],
                'status': 'failed',
                'error': '登录失败或数据提取失败',
                'thread_id': thread_id
            }
            
    except Exception as e:
        print(f"[线程 {thread_id}] 账户 {account_info['username']} 处理异常: {str(e)}")
        return {
            'account': account_info['username'],
            'status': 'error',
            'error': str(e),
            'thread_id': thread_id
        }
    finally:
        loop.close()

async def auto_login_and_extract_with_shared_config(url: str, username: str, password: str, page_size: int, page_count: int, browser_config: BrowserConfig, thread_id: int):
    """
    使用共享浏览器配置的登录和数据提取函数
    """
    # 为每个线程创建唯一的session_id
    session_id = f"shared_session_{thread_id}_{int(time.time())}"
    
    # 其余代码基本与原函数相同，但使用传入的browser_config
    table_schema = {
        "name": "数据表格",
        "baseSelector": "table tr",
        "fields": [
            {"name": "record_id", "selector": "tr td:nth-child(2)", "type": "text"},
        ]
    }

    login_js = f"""
    (async () => {{
        console.log('[线程 {thread_id}] 开始登录流程...');
        
        // 等待页面加载完成
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // 查找用户名输入框
        let usernameInput = document.querySelector('input[name="username"]');
        
        if (usernameInput) {{
            usernameInput.focus();
            usernameInput.value = '';
            usernameInput.value = '{username}';
            usernameInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
            usernameInput.dispatchEvent(new Event('change', {{ bubbles: true }}));
            console.log('[线程 {thread_id}] 用户名已填入');
        }} else {{
            console.log('[线程 {thread_id}] 未找到用户名输入框');
        }}
        
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // 查找密码输入框
        let passwordInput = document.querySelector('input[name="password"]');
        
        if (passwordInput) {{
            passwordInput.focus();
            passwordInput.value = '';
            passwordInput.value = '{password}';
            passwordInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
            passwordInput.dispatchEvent(new Event('change', {{ bubbles: true }}));
            console.log('[线程 {thread_id}] 密码已填入');
        }} else {{
            console.log('[线程 {thread_id}] 未找到密码输入框');
        }}
        
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // 处理滑块验证码
        const sliderSelectors = [
            '.slider-btn',
            '.slide-button', 
            '.slider',
            '.captcha-slider',
            '.drag-btn',
            '.slide-verify',
            '[class*="slider"]',
            '[class*="slide"]',
            '[class*="drag"]'
        ];
        
        let sliderBtn = null;
        for (const selector of sliderSelectors) {{
            sliderBtn = document.querySelector(selector);
            if (sliderBtn) {{
                console.log('[线程 {thread_id}] 找到滑块按钮:', selector);
                break;
            }}
        }}
        
        if (sliderBtn) {{
            const sliderTrack = sliderBtn.closest('.slider-track') || sliderBtn.parentElement;
            const trackRect = sliderTrack.getBoundingClientRect();
            const btnRect = sliderBtn.getBoundingClientRect();
            const slideDistance = trackRect.width - btnRect.width;
            
            console.log('[线程 {thread_id}] 准备滑动距离:', slideDistance);
            
            const mouseDownEvent = new MouseEvent('mousedown', {{
                bubbles: true,
                cancelable: true,
                clientX: btnRect.left + btnRect.width/2,
                clientY: btnRect.top + btnRect.height/2
            }});
            sliderBtn.dispatchEvent(mouseDownEvent);
            
            const steps = 10;
            const stepDistance = slideDistance / steps;
            
            for (let i = 0; i < steps; i++) {{
                await new Promise(resolve => setTimeout(resolve, 50 + Math.random() * 50));
                
                const currentX = btnRect.left + btnRect.width/2 + (i + 1) * stepDistance;
                const mouseMoveEvent = new MouseEvent('mousemove', {{
                    bubbles: true,
                    cancelable: true,
                    clientX: currentX,
                    clientY: btnRect.top + btnRect.height/2
                }});
                document.dispatchEvent(mouseMoveEvent);
            }}
            
            await new Promise(resolve => setTimeout(resolve, 100));
            
            const mouseUpEvent = new MouseEvent('mouseup', {{
                bubbles: true,
                cancelable: true,
                clientX: btnRect.left + btnRect.width/2 + slideDistance,
                clientY: btnRect.top + btnRect.height/2
            }});
            document.dispatchEvent(mouseUpEvent);
            
            console.log('[线程 {thread_id}] 滑块操作完成');
        }} else {{
            console.log('[线程 {thread_id}] 未找到滑块元素');
        }}
        
        await new Promise(resolve => setTimeout(resolve, 3000));
        
        // 查找并点击登录按钮
        const loginBtnSelectors = [
            'button[type="submit"]',
            'input[type="submit"]',
            'button:contains("登录")',
            'button:contains("登陆")', 
            'button:contains("提交")',
            '.login-btn',
            '.submit-btn',
            '#login-btn',
            '#submit'
        ];
        
        let loginBtn = null;
        for (const selector of loginBtnSelectors) {{
            if (selector.includes(':contains')) {{
                const buttons = document.querySelectorAll('button');
                for (const btn of buttons) {{
                    if (btn.textContent.includes('登录') || btn.textContent.includes('登陆') || btn.textContent.includes('提交')) {{
                        loginBtn = btn;
                        console.log('[线程 {thread_id}] 找到登录按钮(文本匹配):', btn.textContent);
                        break;
                    }}
                }}
                if (loginBtn) break;
            }} else {{
                loginBtn = document.querySelector(selector);
                if (loginBtn) {{
                    console.log('[线程 {thread_id}] 找到登录按钮:', selector);
                    break;
                }}
            }}
        }}
        
        if (loginBtn) {{
            loginBtn.click();
            console.log('[线程 {thread_id}] 登录按钮已点击');
        }} else {{
            console.log('[线程 {thread_id}] 未找到登录按钮');
            const form = document.querySelector('form');
            if (form) {{
                form.submit();
                console.log('[线程 {thread_id}] 表单已提交');
            }}
        }}
        
        console.log('[线程 {thread_id}] 登录流程执行完成');
    }})();
    """

    wait_for_login_success = """js:() => {
        const indicators = [
            !document.querySelector('.login-box-body'),
        ];
        
        return indicators.some(indicator => indicator);
    }"""

    # 重试配置
    max_login_attempts = 5
    login_timeout = 15000
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        print(f"[线程 {thread_id}] 正在访问登录页面: {url}")
        
        # 登录重试循环
        login_success = False
        for attempt in range(1, max_login_attempts + 1):
            print(f"[线程 {thread_id}] === 第 {attempt}/{max_login_attempts} 次登录尝试 ===")
            
            try:
                # 每次重试使用新的session_id避免状态污染
                if attempt > 1:
                    pass
                
                login_config = CrawlerRunConfig(
                    session_id=session_id,
                    js_code=login_js,
                    wait_for='.box-body',
                    cache_mode=CacheMode.BYPASS,
                    page_timeout=login_timeout
                )
                
                result = await crawler.arun(url=url, config=login_config)
                
                if result.success:
                    print(f"[线程 {thread_id}] 第 {attempt} 次登录尝试成功！")
                    login_success = True
                    break
                else:
                    error_msg = str(result.error_message).lower()
                    print(f"[线程 {thread_id}] 第 {attempt} 次登录尝试失败: {result.error_message}")
                    
                    # 检查是否是超时或验证相关错误
                    if any(keyword in error_msg for keyword in ['timeout', '超时', 'captcha', '验证']):
                        print(f"[线程 {thread_id}] 检测到超时或验证错误，准备重试...")
                        if attempt < max_login_attempts:
                            print(f"[线程 {thread_id}] 等待 3 秒后进行第 {attempt + 1} 次尝试...")
                            await asyncio.sleep(3)
                    else:
                        print(f"[线程 {thread_id}] 可能是其他类型错误")
                        if attempt < max_login_attempts:
                            await asyncio.sleep(2)
                            
            except Exception as e:
                print(f"[线程 {thread_id}] 第 {attempt} 次登录尝试出现异常: {str(e)}")
                if attempt < max_login_attempts:
                    print(f"[线程 {thread_id}] 等待后重试...")
                    await asyncio.sleep(3)
        
        # 如果所有重试都失败，直接退出
        if not login_success:
            print(f"[线程 {thread_id}] 所有自动登录尝试都失败，程序即将退出...")
            return None

        # 第二步：登录成功后，提取表格数据
        print(f"[线程 {thread_id}] 登录成功，开始提取表格数据...")
        
        extract_config = CrawlerRunConfig(
            session_id=session_id,
            js_only=True,
            table_score_threshold=3,
            word_count_threshold=5,
            excluded_tags=["script", "style", "nav", "footer", "header"],
            extraction_strategy=JsonCssExtractionStrategy(table_schema),
            cache_mode=CacheMode.BYPASS,
            wait_for="table",
            delay_before_return_html=12
        )

        # 构建多个页面的URL
        urls = [url + f"?page_size={page_size}&page={i}" for i in range(1, page_count + 1)]
        print(f"[线程 {thread_id}] 准备抓取 {len(urls)} 个页面的数据...")
        
        # 批量抓取多个页面
        final_results = await crawler.arun_many(urls=urls, config=extract_config)
        
        # 处理每个页面的结果
        all_page_data = []
        failed_pages = []
        
        for i, single_result in enumerate(final_results):
            page_num = i + 1
            current_url = urls[i]
            
            if not single_result.success:
                print(f"[线程 {thread_id}] 第 {page_num} 页数据提取失败: {single_result.error_message}")
                failed_pages.append({"page": page_num, "url": current_url, "error": single_result.error_message})
                continue
            
            # 提取单页数据
            page_data = []
            if single_result.extracted_content:
                try:
                    page_data = json.loads(single_result.extracted_content)
                    print(f"[线程 {thread_id}] 第 {page_num} 页通过提取策略获取到 {len(page_data)} 条数据")
                except json.JSONDecodeError:
                    print(f"[线程 {thread_id}] 第 {page_num} 页提取策略返回的数据不是有效的JSON格式")
                    page_data = []
            
            # 汇总数据
            all_page_data.extend(page_data)

        # 根据某项属性进行去重
        def remove_duplicate(data, key):
            unique_data = []
            unique_record_id = []
            for item in data:
                if item[key] not in unique_record_id:
                    unique_record_id.append(item[key])
                    unique_data.append(item)
            return unique_data

        all_page_data = remove_duplicate(all_page_data, 'record_id')
        
        print(f"[线程 {thread_id}] 数据抓取完成统计:一共抓取到{len(all_page_data)}条数据")
        
        return {
            "url": url,
            "page_size": page_size,
            "page_count": page_count,
            "all_page_data": all_page_data,
        }

def run_multi_account_tasks():
    """
    使用线程池运行多账户任务
    """
    # 加载配置
    config = load_config()
    users = config.get('users', [])
    
    if not users:
        print("配置文件中没有找到用户列表")
        return
    
    # 显示账户信息
    print(f"发现 {len(users)} 个账户:")
    for i, user in enumerate(users, 1):
        print(f"  {i}. {user['username']}")
    
    print(f"\n开始并发处理 {len(users)} 个账户...")
    print(f"浏览器配置: headless={SHARED_BROWSER_CONFIG.headless}")
    print(f"最大并发数: {min(len(users), 3)}")
    print("=" * 60)
    
    # 限制最大并发数，避免系统负载过高
    max_workers = min(len(users), 3)  # 最多3个并发线程
    
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_account = {
            executor.submit(run_single_account_task, user, config): user['username'] 
            for user in users
        }
        
        # 等待任务完成
        for future in as_completed(future_to_account):
            account_name = future_to_account[future]
            try:
                result = future.result()
                results.append(result)
                print(f"账户 {account_name} 任务完成: {result['status']}")
            except Exception as exc:
                print(f"账户 {account_name} 任务异常: {exc}")
                results.append({
                    'account': account_name,
                    'status': 'exception',
                    'error': str(exc)
                })
    
    # 汇总结果
    successful_results = [r for r in results if r['status'] == 'success']
    failed_results = [r for r in results if r['status'] != 'success']
    
    print("\n" + "=" * 60)
    print("多账户任务执行完成!")
    print(f"成功: {len(successful_results)}/{len(users)}")
    print(f"失败: {len(failed_results)}/{len(users)}")
    
    if failed_results:
        print("\n失败账户:")
        for failed in failed_results:
            print(f"  - {failed['account']}: {failed.get('error', '未知错误')}")
    
    # 合并所有成功账户的数据
    all_merged_data = []
    for result in successful_results:
        if result.get('data') and result['data'].get('all_page_data'):
            account_data = result['data']['all_page_data']
            # 为每条数据添加账户信息
            for item in account_data:
                item['source_account'] = result['account']
            all_merged_data.extend(account_data)
    
    # 跨账户去重
    def remove_duplicate_cross_accounts(data, key):
        unique_data = []
        unique_record_id = []
        for item in data:
            if item.get(key) and item[key] not in unique_record_id:
                unique_record_id.append(item[key])
                unique_data.append(item)
        return unique_data
    
    if all_merged_data:
        all_merged_data = remove_duplicate_cross_accounts(all_merged_data, 'record_id')
        print(f"\n合并后总数据量: {len(all_merged_data)} 条 (已去重)")
        
        # 保存合并后的数据
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"multi_account_data_{timestamp}"
        
        combined_result = {
            "timestamp": timestamp,
            "total_accounts": len(users),
            "successful_accounts": len(successful_results),
            "failed_accounts": len(failed_results),
            "total_records": len(all_merged_data),
            "accounts_summary": [
                {
                    "account": r['account'],
                    "status": r['status'],
                    "records": len(r.get('data', {}).get('all_page_data', [])) if r['status'] == 'success' else 0
                }
                for r in results
            ],
            "merged_data": all_merged_data,
            "individual_results": results
        }
        
        asyncio.run(save_to_files(combined_result, filename))
    
    return results

async def save_to_files(data, filename_prefix="table_data"):
    """
    将数据保存到不同格式的文件
    """
    if not data:
        print("没有数据需要保存")
        return
    
    # 保存完整数据为JSON
    json_filename = f"{filename_prefix}_complete.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"完整数据已保存到: {json_filename}")
    

# 保持原有的单账户函数（向后兼容）
async def auto_login_and_extract(url: str, username: str, password: str, page_size: int, page_count: int):
    """
    原有的单账户登录和数据提取函数（向后兼容）
    """
    return await auto_login_and_extract_with_shared_config(
        url=url,
        username=username,
        password=password,
        page_size=page_size,
        page_count=page_count,
        browser_config=SHARED_BROWSER_CONFIG,
        thread_id=0  # 主线程使用ID 0
    )

def main():
    """主函数 - 多账户并发抓取"""
    print("=" * 60)
    print("多账户并发数据爬取工具")
    print("=" * 60)
    
    # 直接运行多账户线程池模式
    run_multi_account_tasks()


if __name__ == "__main__":
    main()
