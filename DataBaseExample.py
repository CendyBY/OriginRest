# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:29:19 2017

@author: Administrator
"""

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
# 导入:
from sqlalchemy import Column, String, create_engine,Float,MetaData,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

apikey = '***'
secretkey = '***'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  
#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)
Testa = okcoinSpot.klines('ltc_cny','1min')
'''
备注：查询时间戳的转换
5分钟内所有https 请求不得超过3000个
每秒提交10个左右
'''


# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'min1kline'
    # 表的结构:
    idkey = Column(String(20), primary_key=True)
    timemark = Column(Float())
    openprice = Column(Float())
    highprice = Column(Float())
    lowprice = Column(Float())
    closeprice = Column(Float())
    tradevol = Column(Float())
    
# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:lh*#123@localhost:3306/btc')

# 创建表
Base.metadata.create_all(engine)
# 查看是否创建成功
engine.table_names()

# 删除表
#Base.metadata.drop_all(engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
'''范例
new_user = User(timemark=1498284720000
                , openprice=331.0
                , highprice=331.8
                , lowprice=330.41
                , closeprice=331.8
                , tradevol=704.608)
session.add(new_user)
'''

# 添加到session:

for i in range(len(Testa)):
    tmp_data = User(idkey =str(i+1)
              ,timemark=Testa[i][0]
               ,openprice=Testa[i][1]
               ,highprice=Testa[i][2]
               ,lowprice=Testa[i][3]
               ,closeprice=Testa[i][4]
               ,tradevol=Testa[i][5])
    session.add(tmp_data)

# 添加所有的session
#session.add_all([user_2, user_3])

# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.timemark<=1498456440000).all()
# 打印类型和对象的name属性:
print('type:', type(user))
print(user.tradevol)
# 关闭Session:
session.close()
