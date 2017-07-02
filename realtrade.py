# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:20:37 2017

@author: Administrator
"""
import sys
sys.path.append('D:\\莱特币API\\REST')
'''
交易步骤：
1.查询最热门交易合约
2.查看账户情况
3.获取数据来源构造交易信号
4.交易记录存档
'''
import time
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
apikey = '***'
secretkey = '***'
okcoinRESTURL = 'www.okex.com'
okcoinSpot = OKCoinFuture(okcoinRESTURL,apikey,secretkey)
k=0
timeflow=[]
priceflow=[]
#init statemachine
statemachine = {'Position':0,'Cost':None,'Limitprice':None,'HistoryHigh':None
                ,'HistoryLow':None}
while True:
    Testa = okcoinSpot.future_klines('ltc_usd','1min','quarter')
    # 开仓信号
    signalstart,openprice,closeprice,limitprice= opensignal(Testa)
    # 平仓信号
    signalend = closesignal(Testa,statemachine)

    # 综合信号
    finalsignal = compresignal(signalstart,signalend,statemachine)
    # 状态机更新
    statemachine = machinefresh(finalsignal,Testa,statemachine)
    # 下单信号
    print(str(finalsignal))
    time.sleep(15)

def machinefresh(finalsignal,Testa,statemachine):
    if finalsignal == 1 :#更新
        if statemachine['Position']==0:#开仓
            pass
        elif statemachine['Position']==-1:#平仓
            pass
        else:
            pass
    elif finalsignakl=-1:
        if statemachine['Position']==0:#开仓
            pass
        elif statemachine['Position']==1:#平仓
            pass
        else:
            pass
    elif finalsignal == 0:
        pass


def compresignal(signalstart,signalend,statemachine):
    if signalstart!=0 and statemachine['Position']==0:#有开仓信号
        if signalstart==1:
            return 1
        elif signalstart==-1:
            return -1
    elif signalend!=0 and statemachine['Position']!=0:#有平仓信号
        if statemachine['Position']==1 and signalend==-1:
            return -1
        elif statemachine['Position']==-1 and signalend==1:
            return 1
        else:
            return 0
    else:
        return 0





def opensignal(Testa):
    openprice = [x[1] for x in Testa[-3:]]
    closeprice = [x[4] for x in Testa[-3:]]
    redthree = [1 if closeprice[i]>openprice[i] else 0 for i in range(len(openprice))]
    bluethree = [1 if closeprice[i]<openprice[i] else 0 for i in range(len(openprice))]
    limitprice = openprice[0]
    if sum(redthree) == 3:
        return 1,openprice,closeprice,limitprice
    elif sum(bluethree) == 3:
        return -1,openprice,closeprice,limitprice
    else:
        return 0,openprice,closeprice,limitprice
            
def closesignal(Testa,statemachine):
    judgeprice = Testa[-1][4]
    if statemachine['Position']!=0:
        #止损止盈
        if statemachine['Position']>0:               
            if judgeprice - statemachine['Cost']> 1:
                winprice = statemachine['HistoryHigh']-0.3*(statemachine['HistoryHigh']-statemachine['Cost'])
            else:
                winprice = statemachine['Limitprice']
            lossprice = statemachine['Limitprice']
            if judgeprice<lossprice or judgeprice<winprice:
                print('出现平仓信号')
                return -1
            else:
                pass     
        elif statemachine['Position']<0:
            if judgeprice - statemachine['Cost'] < 1:
                winprice = statemachine['HistoryLow']+0.3*(statemachine['Cost']-statemachine['HistoryLow'])
            else:
                winprice = statemachine['Limitprice']
            lossprice = statemachine['Limitprice']

            if judgeprice>lossprice or judgeprice >winprice:#止损出场
                print('出现平仓信号')
                return 1
            else:
                pass
    else:
        return 0
    
            
            

    
    