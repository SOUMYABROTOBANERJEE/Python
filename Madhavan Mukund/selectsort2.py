# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 00:56:09 2018

@author: soumy
"""

def selectionsort2(a):
    
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                print(a)
                (a[j],a[i])=(a[i], a[j])
    print(a)