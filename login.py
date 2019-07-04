#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

import requests

def login():
    url = 'https://passport.mbalib.com/api/login'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {'username': 'SusanTest1', 'password': '123456'}
    response = requests.post(url, headers=header, data=data)
    your_dict = json.loads(response.text)
    #返回token
    token=your_dict["access_token"]
    return token
