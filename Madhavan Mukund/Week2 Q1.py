# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:44:45 2018

@author: soumy
"""

def func():
    n=input()
    r=0
    while(n>0):
        d=n%10
        r*=10+d
        n//=10
    print("Reverse string=",r)
        
        