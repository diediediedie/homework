#!/usr/bin/env python
# -*- coding: utf8 -*-
def isPrime(N):
	for y in range(2,N):
		if(N%y==0):
			prime=0
			return 0
			break
		else:
			prime=1
			return 1
	
sum=0
for x in range(2,1001):
	if isPrime(x)==1:
		sum+=x;	
	else:
		sum=sum
print sum
		
	
