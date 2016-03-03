#!/usr/bin/env python
# -*- coding: utf8 -*-
f=open("ATM.txt","a")
print u'您的存款為$5000'
print u'您欲提款金額為: '
num=input()
if (5000-num)<0:
	print u'您的存款不足!'
	f.write("您欲提款金額為:%d\n,存款不足!!!!" %(num))
elif (5000-num)==0:
	print u'您的存款無剩餘存款!'
	f.write("您欲提款金額為:%d\n,沒存款囉~" %(num))
else:
	print u'您的存款還剩%d~哈哈' %(5000-num)
	f.write("您欲提款金額為:%d\n,還剩%d" %(num,5000-num))

f.close