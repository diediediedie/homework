#!/usr/bin/env python
# -*- coding: utf8 -*-

f=open("input.txt","r")

n=f.readline()
a=n.count(" ")
b=n.count('e')
c=len(n)
f.close()

print u'空白出現%d次' %a
print u'e出現%d次' %b
print u'共%d個字元' %c

print u'空白佔整體比例%f' %(a/c)
print u'e佔整體比例%f' %(b/c)