# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:37:25 2017

@author: Administrator
"""

import time
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
from sqlalchemy import Column, String, create_engine,Float,MetaData,Integer,BIGINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
apikey = '975359f4-fc3f-4941-b66d-d2643eb2fe7c'
secretkey = 'E79EB99F9162B096096BDF71EC16BACC'
okcoinRESTURL = 'www.okcoin.cn'
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)
engine = create_engine('mysql+pymysql://root:lh*#123@localhost:3306/btc')
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
class DataFresh(Base):
    __tablename__ = 'min1kline_ltc'
    idkey = Column(Integer(), primary_key=True)
    timemark = Column(BIGINT())
    openprice = Column(Float())
    highprice = Column(Float())
    lowprice = Column(Float())
    closeprice = Column(Float())
    tradevol = Column(Float())
    count = Column(BIGINT())
    
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
    count = Column(BIGINT())

class DepthFresh(Base):
    __tablename__ = 'depth'
    idkey = Column(Integer(), primary_key=True)
    buy1p = Column(Float())
    buy1v = Column(Float())
    sell1p = Column(Float())
    sell1v = Column(Float())
    count = Column(BIGINT())
   
    
Base.metadata.create_all(engine)
print(engine.table_names())

count=0
while True:
    Testa = okcoinSpot.klines('ltc_cny','1min')
    Testticker = okcoinSpot.ticker('ltc_cny')
    Testdepth = okcoinSpot.depth('ltc_cny')
    session = DBSession()
    userkline = session.query(DataFresh).all()
    userticker = session.query(TickerFresh).all()
    userdepth = session.query(DepthFresh).all()
    count = count +1
    for i,j in enumerate(Testa):
            tmp_data = DataFresh(idkey = len(userkline)+i+1
                ,timemark=j[0]
               ,openprice=j[1]
               ,highprice=j[2]
               ,lowprice=j[3]
               ,closeprice=j[4]
               ,tradevol=j[5]
                ,count = count)
            session.add(tmp_data)
            
    tmp_data = TickerFresh(idkey = len(userticker)+1
        ,date=int(Testticker['date'])
       ,buyprice=float(Testticker['ticker']['buy'])
       ,highprice=float(Testticker['ticker']['high'])
       ,lastprice=float(Testticker['ticker']['last'])
       ,lowprice=float(Testticker['ticker']['low'])
       ,sellprice=float(Testticker['ticker']['sell'])
       ,tradevol=float(Testticker['ticker']['vol'])
        ,count = count)
    session.add(tmp_data)
    
    tmp_data = DepthFresh(idkey = len(userdepth)+1
       ,buy1p=float(Testdepth['asks'][len(Testdepth['bids'])-1][0])
       ,buy1v=float(Testdepth['asks'][len(Testdepth['bids'])-1][1])
       ,sell1p=float(Testdepth['bids'][0][0])
       ,sell1v=float(Testdepth['bids'][0][1])
        ,count = count)
    session.add(tmp_data)
    print(str(count))