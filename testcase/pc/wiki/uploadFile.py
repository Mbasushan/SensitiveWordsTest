#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
import time
import testcase.tool.isElement as isElement
from selenium.webdriver import ActionChains

import testcase.pc.login as login

class UploadFile(unittest.TestCase):

    def setUp(self):
        base_url = 'https://passport.mbalib.com'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        self.driver.maximize_window()
        login.loginText(self)

    def test_uploadImages(self):
        """百科上传文件"""
        driver = self.driver
        driver.get("https://wiki.mbalib.com")
        time.sleep(5)
        # 关闭橱窗广告
        ad_close = isElement.find_Element(self, 'id', 'ad-close')
        if ad_close:
            driver.find_element_by_id('ad-close').click()
        # 点击工具箱
        # 准备悬停的元素
        move_element = driver.find_element_by_css_selector("div#p-tb>h5")
        # 悬停
        ActionChains(driver).move_to_element(move_element).perform()
        driver.find_element_by_link_text("上传文件").click()
        time.sleep(10)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()