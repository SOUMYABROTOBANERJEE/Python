# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:29:59 2018

@author: soumy
"""
def isprime(n):
    c=0
    #p=n[0]
    if n==0 or n==1 or n<0:
        return -1
    for i in range (2,n//2+1):
        if n%i == 0:
            c=c+1
            break
    return c
        
def sumprimes(l):
   try:
    sum=0
    for i in range (len(l)):
        
        if isprime(l[i])==0:
         #print(l[i])
         sum+=l[i]
    return sum
   except :
       print("Enter a Number")

         
         