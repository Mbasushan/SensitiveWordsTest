#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import testcase.tool.isElement as isElement
from selenium.webdriver import ActionChains
from PIL import Image
import pytesseract
import os

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
        driver.save_screenshot('C:/AutomatedTesting/SensitiveWordsTest/image/screen.png')
        imgelement = driver.find_element_by_xpath('//*[@id="upload"]/table/tbody/tr[4]/td[2]/img')  # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open("C:/AutomatedTesting/SensitiveWordsTest/image/screen.png")  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save('C:/AutomatedTesting/SensitiveWordsTest/image/imgCode.png')  # 保存我们接下来的验证码图片 进行打码
        codeimg = Image.open('C:/AutomatedTesting/SensitiveWordsTest/image/imgCode.png')
        # 把彩色图像转化为灰度图像。RBG转化到HSI彩色空间，采用I分量
        imgry = codeimg.convert('L')
        # 图片转为字符串
        code = pytesseract.image_to_string(imgry)
        time.sleep(5)
        print('code:', code)
        # 点击【选择文件】
        driver.find_element_by_id('wpUploadFile').click()
        time.sleep(10)
        os.system("C:/AutomatedTesting/SensitiveWordsTest/testcase/tool/upfile.exe")
        time.sleep(10)
        # 目标文件名
        driver.find_element_by_id('wpDestFile').clear()
        driver.find_element_by_id('wpDestFile').click()
        driver.find_element_by_id('wpDestFile').send_keys('上传违规图片.jpg')
        # 文件描述
        driver.find_element_by_id('wpUploadDescription').click()
        driver.find_element_by_id('wpUploadDescription').send_keys('自动化测试上传违规图片是否拦截')
        time.sleep(5)
        # 填写验证码
        driver.find_element_by_name('wpCode').click()
        driver.find_element_by_name('wpCode').send_keys(code)
        time.sleep(3)
        driver.find_element_by_name('wpUpload').click()
        time.sleep(10)
        # 上传文件后返回值
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        res = soup.select_one('#content > div.firstHeading-wrap > h1')
        print("res", res)
        text='图片内容不合法'
        if text in res:
            print("拦截图片内容不合法")
        else:
            print("图片内容不合法未拦截")
        # 删除验证码图片
        os.remove('C:/AutomatedTesting/SensitiveWordsTest/image/screen.png')
        os.remove('C:/AutomatedTesting/SensitiveWordsTest/image/imgCode.png')


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()