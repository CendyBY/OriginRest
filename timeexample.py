# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:25:09 2017

@author: Administrator
"""
import time

#时间戳转化和分解

time.asctime(b[1]/1000)

#显示时间
time.ctime(b[1]/1000)

#返回时间元组t
time.gmtime(b[1]/1000)

#返回时间元组t
time.localtime(b[1]/1000)

#返回时间戳
time.mktime(time.localtime(b[1]/1000))

#格式
fmt='%Y.%m.%d %H:%M:%S '
time.strftime(fmt,time.localtime(b[1]/1000))

# 时间字符串转换
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print(struct_time)