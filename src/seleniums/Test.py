#!/usr/local/bin/python3.7

from selenium import webdriver
import time

# phantomJS路径
path = '/Users/liujie/Documents/soft/phantomjs-2.1.1-macosx/bin/phantomjs'
# 创建浏览器对象
browser = webdriver.PhantomJS(path)

# 打开百度并操作
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(1)
# 截图
browser.save_screenshot('baidu.png')
# 定位搜索框
search = browser.find_element_by_id('kw')
time.sleep(1)
# 在搜索框输入内容
search.send_keys('美女')
time.sleep(1)
# 截图
browser.save_screenshot('meinv.png')
# 关闭浏览器
browser.quit()
