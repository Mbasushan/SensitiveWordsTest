#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import time
import testcase.pc.login as login
import testcase.tool.isElement as isElement
import testcase.tool.gl as gl

class Comments(unittest.TestCase):

    def setUp(self):
        base_url = 'https://passport.mbalib.com'
        self.driver = webdriver.Chrome(gl.chrome_URL)
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        self.driver.maximize_window()
        login.loginText(self)

    def test_news_comments(self):
        """资讯评论"""
        driver=self.driver
        driver.get("https://news.mbalib.com/story/246770")
        #将页面滚动条拖到底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.find_element_by_id("scomment").click()
        driver.find_element_by_id("scomment").send_keys("思明区红灯区")
        driver.find_element_by_css_selector("div#vcontent>div:nth-child(2)>button").click()
        time.sleep(5)
        al = driver.switch_to_alert()
        time.sleep(10)
        text = al.text
        if text == '操作失败，含有敏感词':
            print("该评论存在敏感词，被拦截")
        else:
            print("该评论不存在敏感词")
        time.sleep(3)
        al.accept()

    def test_wiki_comments(self):
        """百科评论"""
        driver = self.driver
        driver.get("https://wiki.mbalib.com/wiki/测试")
        #关闭橱窗广告
        ad_close = isElement.find_Element(self, 'id', 'ad-close')
        if ad_close:
            driver.find_element_by_id('ad-close').click()
        # 将页面滚动条拖到底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_css_selector("form#commentform>textarea").click()
        driver.find_element_by_css_selector("form#commentform>textarea").send_keys("思明区红灯区")
        driver.find_element_by_name('submit').click()
        time.sleep(5)
        title=driver.title
        print("title:",title)
        if title=="评论 - MBA智库百科":
            print("该评论存在敏感词，被拦截")
        else:
            print("该评论不存在敏感词")

    def test_ketang_comments(self):
        """课堂评论"""
        driver = self.driver
        driver.get("https://ke.mbalib.com/course/8439963")
        driver.find_element_by_link_text('开始学习').click()
        time.sleep(5)
        driver.find_element_by_link_text('评论').click()
        time.sleep(3)
        driver.find_element_by_css_selector('div.comment-footbar>div>div>input').click()
        time.sleep(3)
        driver.find_element_by_id('comment').click()
        driver.find_element_by_id('comment').send_keys("湖里区红灯区")
        driver.find_element_by_link_text('发布').click()
        time.sleep(5)
        # 判断获取弹窗提示内容
        time.sleep(5)
        elem = driver.find_element_by_id('show_notice')
        txts = str(elem.get_attribute('textContent'))
        if txts== '操作失败，含有敏感词':
            print("该评论存在敏感词，被拦截")
        else:
            print("该评论不存在敏感词")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()