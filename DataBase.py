# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 09:30:29 2017

@author: Administrator
"""
'''
把查询数据导入到数据库存储
'''
import pymysql
#1 链接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='lh*#123'
                       , db='BTC')
#2 创建表

create table tb1(
              nid int not null defalut 2,
              num int not null
          )


from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:lh*#123@localhost:3306/BTC')