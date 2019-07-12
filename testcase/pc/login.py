#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
import time

def login():
    driver = webdriver.Chrome()
    driver.get("https://passport.mbalib.com")
    driver.maximize_window()
    driver.find_element_by_id('mobile_text').send_keys("13106445986")
    driver.find_element_by_id('hide_mobile_password').click()
    driver.find_element_by_id('mobile_password').send_keys('123456')
    time.sleep(3)
    driver.find_element_by_id('login_sub').click()
    cookie = driver.get_cookies()
    print(cookie)
    return cookie

def loginText(self):
    driver=self.driver
    driver.find_element_by_id('mobile_text').send_keys("13106445986")
    driver.find_element_by_id('hide_mobile_password').click()
    driver.find_element_by_id('mobile_password').send_keys('123456')
    time.sleep(3)
    driver.find_element_by_id('login_sub').click()
    time.sleep(10)