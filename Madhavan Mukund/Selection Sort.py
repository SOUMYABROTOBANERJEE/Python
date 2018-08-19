# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 00:45:19 2018

@author: soumy
"""

def selectionsort(l):
    for i in range(len(l)):
        min=l[i]
        for j in range (min+1, len(l)):
            if l[j]<l[min] :
                min=j
            (l[min],l[i])=(l[i],l[min])
    print(l)
            