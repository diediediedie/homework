#!/usr/bin/env python
# -*- coding: utf8 -*-
import random
n=random.randint(1,99),
print u'終極密碼start!!!!'
print u'請輸入你猜的數字'
x = input()
count=0
a=1
b=99
while n!=x:
	
	if x>n:
		a=x
		print u'範圍%d~%d' %(a,b) 
		count=count+1
		print u'請輸入你猜的數字'
		x = input()
	elif x<n:
		b=x
		print u'範圍%d~%d' %(a,b) 
		count=count+1
		print u'請輸入你猜的數字'
		x = input()
	
	print u'你猜中了!共猜了%d次' %count
		
	