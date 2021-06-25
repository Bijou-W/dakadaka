
# pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
import time
import sys
import string
 
 
def tick(driver, id, passw):
    driver.get("https://stuhealth.jnu.edu.cn/#/login")
    driver.find_element_by_id('zh').send_keys(id)
    driver.find_element_by_id('passw').send_keys(passw)
    # 登录
    driver.find_element_by_id('passw').send_keys(Keys.ENTER)
    # 等待新页面加载完毕
    time.sleep(3)
 
    # 填表
 
    # driver.find_element_by_id('10000').click()
    # 如果页面跳转到新窗口，需要重定位
    # time.sleep(3)
    # search_window = driver.current_window_handle  # 此行代码用来定位当前页面
    # html =driver.page_source
    # print("打印标题")
    # print(driver.title)
    if driver.current_url == 'https://stuhealth.jnu.edu.cn/#/index':
        driver.find_element_by_id('10000').send_keys(Keys.SPACE)
        # 提交
        driver.find_element_by_id('tj').click()
        time.sleep(2)
    if driver.current_url == 'https://stuhealth.jnu.edu.cn/#/index/complete':
 
        print(id + ',打卡成功！')
    else:
        print(id + ',打卡失败！')
 
 
# 使用浏览器驱动，启动Chrome
# 需要下载对应版本的驱动。
# 1.地址栏输入，chrome://version/，查看自己的版本
# 2.在列表中下载对应版本的驱动exe文件，http://chromedriver.storage.googleapis.com/index.html
# 3.将所下载文件放入Python/Lib目录下，并将此目录 添加到环境变量PATH
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome()
# Firefox
# driver = webdriver.Firefox()
# 浏览器后台运行
# option=webdriver.ChromeOptions()
# option.add_argument('headless') # 设置option
# driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器
# 填表
 
#filename = ".\\id+passw.txt"
#with open(filename, 'r') as f:
    #lines = f.readlines()
    #for line in lines:
        #if line.startswith('#'):
           # continue
       # id = line.split(' ')[0]
      #  passw = line.split(' ')[1]
       # tick(driver, id, passw)
 
driver.close()
sys.exit()
