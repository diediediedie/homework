#!/usr/bin/env python
# -*- coding: utf8 -*-
x=input('input a number:')
for y in range(2,x):
	if(x%y==0):
		prime=0
		break
	else:
		prime=1
if(prime==0):
	print u'不是質數'
else:
	print u'是質數'
	