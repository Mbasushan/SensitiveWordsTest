#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

import requests
import login

def news_comments():
    """资讯评论接口"""
    token=login.login()
    url = 'https://news.mbalib.com/api/SubmitComment'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {'article_id': '238423', 'content': '威尼斯','access_token':token}
    response = requests.post(url, headers=header, data=data)
    text = json.loads(response.text)
    print(text)

def wiki_comments():
    """百科评论接口"""
    token = login.login()
    url = 'https://wiki.mbalib.com/client'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {'app': '1', 'format':'json','action':'comment','key':'七层次领导力','content': '威尼斯','parentid':'0', 'access_token': token}
    response = requests.post(url, headers=header, data=data)
    text = json.loads(response.text)
    print(text)

def ketang_comments():
    """课堂评论接口"""
    token = login.login()
    url = 'https://ke.mbalib.com/api/addComment'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {'id': '8641326', 'comment': '威尼斯', 'access_token': token}
    response = requests.post(url, headers=header, data=data)
    text = json.loads(response.text)
    print(text)

def nicnName():
    """修改昵称接口"""
    token = login.login()
    url = 'https://passport.mbalib.com/api2/setUserInfo'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {'field': 'nickname', 'value': '威尼斯', 'access_token': token}
    response = requests.post(url, headers=header, data=data)
    text = json.loads(response.text)
    print(text)

def avata():
    """修改头像接口"""
    token = login.login()
    url = 'https://passport.mbalib.com/api2/setUserInfo'
    #以2进制方式打开图片
    with open('F:/图片/3.jpg', "rb")as f_abs:
        body = {'value': ('3.jpg', f_abs, 'image/jpg')}
        data={'access_token': token,"field": 'avata'}
        response = requests.post(url=url,data=data,files=body)
        text = json.loads(response.text)
        print(text)


if __name__ == '__main__':
    #news_comments()
    #ketang_comments()
    #wiki_comments()
    #nicnName()
    avata()