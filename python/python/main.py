# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

def main():
    driver = webdriver.Chrome()                                                     #浏览器驱动打开google浏览器
    driver.get("http://10.110.2.15/forum.php")                                      #获取地址
    driver.maximize_window()                                                        #最大化窗口
    driver.find_element_by_xpath('//*[@id="nv_forum"]/div[7]/a[2]').click()         #关闭右侧广告窗口
    time.sleep(3)                                                                   #等待时间

    # 论坛账号密码
    driver.find_element_by_id('ls_username').send_keys("这里写论坛账号")
    driver.find_element_by_id('ls_password').send_keys("这里写论坛密码")
    time.sleep(5)

    #点击“登陆”按钮
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button'))).click()
    time.sleep(3)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mn_N00b5"]'))).click()        #
    driver.switch_to.window(driver.window_handles[1])                               #切换标签页的元素
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/button[2]').click()      #关闭弹出公告窗口

    #校园网账号密码
    driver.find_element_by_id('1').send_keys("这里写校园网账号")
    driver.find_element_by_id('2').send_keys("这里写校园网密码")
    driver.find_element_by_xpath('/html/body/div[2]/div[4]').click()                #登陆认证

    time.sleep(10)

if __name__ == '__main__':
    main()
os.system(r"C:\Users\Administrator\Desktop\HotPoint\wifi.bat")                      #开启热点
