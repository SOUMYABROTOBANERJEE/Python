# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:44:45 2018

@author: soumy
"""

def intreverse(n):
    try:
        #p=input("Enter the number:")
        r=0
        #n=int (p)
        if(n<0):
            print("positive numbers only")
            n=-n
        while(n>0):
            d=n%10
            r=r*10+d
            n//=10
        return r
    except ValueError:
        print("Not a number")
        
        