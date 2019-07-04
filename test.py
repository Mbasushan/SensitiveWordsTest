#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import urllib.request

import lxml
import os
import unittest
from lxml import etree
from lxml.etree import HTMLParser
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import testcase.tool.isElement as isElement
import pytesser3
from PIL import Image
from bs4 import BeautifulSoup


import testcase.pc.login as login

class Comments(unittest.TestCase):

    def setUp(self):
        base_url = 'https://passport.mbalib.com'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        self.driver.maximize_window()
        login.loginText(self)


    def test_comments(self):
        """修改头像"""
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
        #获取到页面元素代码
        tree = driver.page_source
        soup = BeautifulSoup(tree, 'lxml')
        #定位到图片img
        tag = soup.select_one('#upload > table > tbody > tr:nth-child(4) > td:nth-child(2) > img')
        #获取到图片地址
        imgCodeUrl=tag.get('src')
        imgCodeUrl=imgCodeUrl.replace('//','')
        print("downUrlString",imgCodeUrl)
        #保存到项目
        urllib.request.urlretrieve(imgCodeUrl, 'D:/SensitiveWords/image/imgCode.jpg')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()