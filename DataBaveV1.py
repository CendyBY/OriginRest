#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:20:56 2017

@author: Administrator
"""

'''
数据更新步骤：
1.查询数据库是否有这个表名
2.提取表中最新的一条数据
3.网页请求数据
4.K线数据是否更新
5.更新数据库
'''

'''
需要存储的数据有：
1.合约行情数据
2.合约深度信息
3.
'''
from sqlalchemy import Column, String, create_engine,Float,MetaData,Integer,BIGINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time
class DataBaseV(object):
    def __init__(self, TableName, StrName, Data):
        """
        Constructor for class of DataBase.
        :param TableName: TableName
        :param StrName: String of data
        :param Data: data for saving
        :return: Object of OKFuture
        """
        self.__TableName = TableName
        self.__StrName = StrName
        self.__Data = Data
        
    def inittable(self,):
        engine = create_engine('mysql+pymysql://root:lh*#123@localhost:3306/btc')
        