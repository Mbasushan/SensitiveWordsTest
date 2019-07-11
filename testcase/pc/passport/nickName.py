#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import unittest
from selenium import webdriver
import time
import testcase.pc.login as login
import testcase.tool.gl as gl

class Passport(unittest.TestCase):

    def setUp(self):
        base_url = 'https://passport.mbalib.com'
        self.driver = webdriver.Chrome(gl.chrome_URL)
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        self.driver.maximize_window()
        login.loginText(self)

    def test_nickName(self):
        """修改昵称"""
        driver=self.driver
        driver.find_element_by_link_text('修改个人信息').click()
        time.sleep(3)
        driver.find_element_by_id('nickname_modify').click()
        driver.find_element_by_css_selector('div#nickname_lay2>input').send_keys("红灯区")
        driver.find_element_by_css_selector('div#nickname_lay2>button').click()
        time.sleep(5)
        elem = driver.find_element_by_css_selector('div#code_err>span')
        txts = str(elem.get_attribute('textContent'))
        if txts == '操作失败，含有敏感词':
            print("该昵称存在敏感词，被拦截")
        else:
            print("该昵称不存在敏感词")

    def test_headPhoto(self):
        """修改头像"""
        driver = self.driver
        driver.find_element_by_link_text('修改个人信息').click()
        time.sleep(3)
        now_handle = driver.current_window_handle
        driver.find_element_by_id('avatar_modify').click()
        all_handles = driver.window_handles  # 获取所有窗口句柄
        print(all_handles)
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                driver.find_element_by_css_selector("label.ui_button").click()
                time.sleep(5)
                #打开图片
                os.system(gl.upfile_URL)
                time.sleep(10)
                driver.find_element_by_link_text("确定").click()
                # 判断是否有选择图片
                #al = driver.switch_to_alert()
                #time.sleep(10)
                #text = al.text
                #if text == "还未选择图片":
                    #print("未选择图片")
                    #return
        time.sleep(5)
        handles = driver.window_handles  # 获取所有窗口句柄
        print("handles:", handles)
        driver.switch_to_window(handles[0])
        elem = driver.find_element_by_css_selector('div#code_err>span')
        txts = str(elem.get_attribute('textContent'))
        if txts == '操作失败，图片不合法':
            print("该图片不合法，被拦截")
        else:
            print("该图片合法")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()