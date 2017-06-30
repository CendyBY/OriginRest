# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:54:31 2017

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
import time
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
from sqlalchemy import Column, String, create_engine,Float,MetaData,Integer,BIGINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
apikey = '***'
secretkey = '***'
okcoinRESTURL = 'www.okcoin.cn'
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)
engine = create_engine('mysql+pymysql://root:lh*#123@localhost:3306/btc')
Base = declarative_base()
class DataFresh(Base):
    __tablename__ = 'min1klinefresh3'
    idkey = Column(Integer(), primary_key=True)
    timemark = Column(BIGINT())
    openprice = Column(Float())
    highprice = Column(Float())
    lowprice = Column(Float())
    closeprice = Column(Float())
    tradevol = Column(Float())

class DataFresh(Base):
    __tablename__ = 'min1kline_ltc'
    idkey = Column(Integer(), primary_key=True)
    timemark = Column(BIGINT())
    openprice = Column(Float())
    highprice = Column(Float())
    lowprice = Column(Float())
    closeprice = Column(Float())
    tradevol = Column(Float())
    
class TickerFresh(Base):
    __tablename__ = 'ticker'
    idkey = Column(Integer(), primary_key=True)
    date = Column(BIGINT())
    buyprice = Column(Float())
    highprice = Column(Float())
    lastprice = Column(Float())
    lowprice = Column(Float())
    sellprice = Column(Float())
    tradevol = Column(Float())

class DepthFresh(Base):
    __tablename__ = 'depth'
    idkey = Column(Integer(), primary_key=True)
    date = Column(BIGINT())
    buyprice = Column(Float())
    highprice = Column(Float())
    lastprice = Column(Float())
    lowprice = Column(Float())
    sellprice = Column(Float())
    tradevol = Column(Float())
    
Base.metadata.create_all(engine)
print(engine.table_names())
DBSession = sessionmaker(bind=engine)
fmt='%Y.%m.%d %H:%M:%S '
print('程序开始时间：'+time.strftime(fmt,time.localtime(time.time())))
starttime = time.strftime(fmt,time.localtime(time.time()))
countn=0
compare = set()
while True:
    Testa = okcoinSpot.klines('ltc_cny','1min')
    Testticker = okcoinSpot.ticker('ltc_cny')
    Testdepth = okcoinSpot.depth('ltc_cny')
    
    session = DBSession()
    # 先提取数据
    user = session.query(DataFresh).all()
    if len(user)>0:
        for i in user:
            compare.add(i.timemark)
            
    for i,j in enumerate(Testa):
        if j[0] in compare:
#            print('第'+str(i)+'在序列中')
        else:
            print('第'+str(i)+'bu在序列中')
            #添加到数据库中
            tmp_data = DataFresh(idkey = len(user)+i+1
                ,timemark=j[0]
               ,openprice=j[1]
               ,highprice=j[2]
               ,lowprice=j[3]
               ,closeprice=j[4]
               ,tradevol=j[5])
            session.add(tmp_data)
    session.commit()
    session.close()
    print('当地时间：'+time.strftime(fmt,time.localtime(time.time())))
    countn+=1
    print('提交次数'+str(countn))
            
        
    
    
    
    
