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
import testcase.pc.conmments.conmments as comments
import testcase.pc.wiki.uploadFile as uploadFile


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
        """test"""
        #comments.Comments.test_wiki_comments(self)
        uploadFile.UploadFile.test_uploadImages(self)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()