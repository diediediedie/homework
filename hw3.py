#!/usr/bin/env python
# -*- coding: utf8 -*-
a=1
b=1
for x in range(1,56):
	if b<a:
		print x,
		b+=1
	else:
		print x
		a+=1
		b=1