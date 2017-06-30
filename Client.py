#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

#初始化apikey，secretkey,url
apikey = '975359f4-fc3f-4941-b66d-d2643eb2fe7c'
secretkey = 'E79EB99F9162B096096BDF71EC16BACC'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  
okcoinFutureURL = 'www.okex.com' 
#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinFutureURL,apikey,secretkey)

# 品种参数
Species = ('btc_cny','ltc_cny','eth_cny')
Types = ('1min',
             '3min',
             '5min',
             '15min',
             '30min',
             '1day',
             '3day',
             '1week',
             '1hour',
             '2hour',
             '4hour',
             '6hour',
             '12hour'
             )

i=1
#print (u' 现货行情 ')
#print (okcoinSpot.ticker(Species[0]))

#print (u' 现货深度 ')
#print (okcoinSpot.depth(Species[0]))
#
#print (u' 现货历史交易信息 ')
#print (okcoinSpot.trades(Species[i]))

#print (u' 现货历史交易信息 ')
#print (okcoinSpot.klines(Species[1],Types[0]))
#Testa = okcoinSpot.klines(Species[1],Types[0])
#返回的是时间戳，开高低收量
#print (u' 用户现货账户信息 ')
#print (okcoinSpot.userinfo())

#print (u' 现货下单 ')
#print (okcoinSpot.trade('ltc_usd','buy','0.1','0.2'))

#print (u' 现货批量下单 ')
#print (okcoinSpot.batchTrade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

#print (u' 现货取消订单 ')
#print (okcoinSpot.cancelOrder('ltc_usd','18243073'))

#print (u' 现货订单信息查询 ')
#print (okcoinSpot.orderinfo(Species[i],'18243644'))

#print (u' 现货批量订单信息查询 ')
#print (okcoinSpot.ordersinfo('ltc_usd','18243800,18243801,18243644','0'))

#print (u' 现货历史订单信息查询 ')
#print (okcoinSpot.orderHistory('ltc_usd','0','1','2'))

#print (u' 期货行情信息')
print (okcoinFuture.future_ticker('ltc_usd','this_week'))

#print (u' 期货市场深度信息')
print (okcoinFuture.future_depth('ltc_usd','quarter','6'))

#print (u'期货交易记录信息') 
#print (okcoinFuture.future_trades('ltc_usd','this_week'))

#print (u'期货指数信息')
#print (okcoinFuture.future_index('ltc_usd'))

#print (u'美元人民币汇率')
#print (okcoinFuture.exchange_rate())

#print (u'获取预估交割价') 
#print (okcoinFuture.future_estimated_price('ltc_usd'))

#print (u'获取全仓账户信息')
print (okcoinFuture.future_userinfo())

#print (u'获取全仓持仓信息')
print (okcoinFuture.future_position('ltc_usd','quarter'))

#print (u'期货下单')
print (okcoinFuture.future_trade('ltc_usd','quarter','40.00','1','1','0','10'))
# amount:合约张数
# price：美元计价
print (okcoinFuture.future_trade(symbol='ltc_usd',contractType='quarter',
 price='40',amount='1',tradeType='1',matchPrice='0',leverRate='10'))
#print (u'期货批量下单')
#print (okcoinFuture.future_batchTrade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

#print (u'期货取消订单')
print (okcoinFuture.future_cancel('ltc_usd','quarter','6896600986'))

#print (u'期货获取订单信息')
print (okcoinFuture.future_orderinfo('ltc_usd','quarter','6896592048','0','1','2'))
(symbol,contractType,orderId,status,currentPage,pageLength):

print (okcoinFuture.future_orderinfo('ltc_usd','quarter',
orderId = '6896592048',status = '0',currentPage='1',pageLength='2'))
#orderId：订单ID -1:查询指定状态的订单，否则查询相应订单号的订单
#status：1:未完成的订单 2:已经完成的订单
#currentPage：当前页数
#pageLength：每页获取条数，最多不超过50

#print (u'期货逐仓账户信息')
#print (okcoinFuture.future_userinfo_4fix())

#print (u'期货逐仓持仓信息')
#print (okcoinFuture.future_position_4fix('ltc_usd','quarter',2))



   
