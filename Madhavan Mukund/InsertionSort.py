# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 01:10:33 2018

@author: soumy
"""

def InsertionSort(l):
    for i in range(len(l)):
        pos=i
        while pos>0 and l[pos]<l[pos-1]:
            pos-=1
    print(l)

l=list(range(10,1,-2))