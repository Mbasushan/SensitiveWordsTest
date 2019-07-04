#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
#从数据库获取数据

#链接数据库
conn = pymysql.connect(host='192.168.1.158',port=3306,user='wikiuser',passwd='amoy@china4com',db='wikidb')

cursor = conn.cursor()
cursor.execute('SELECT user_id FROM ketang_user')
datalist = []
qryset = cursor.fetchall()
#查询到的数据保存为list
for s in qryset:
    datalist.append(s[0])
print("yzm",datalist)
cursor.close()
conn.close()
