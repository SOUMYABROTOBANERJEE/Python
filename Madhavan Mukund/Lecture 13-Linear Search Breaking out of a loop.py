# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def findpos(l,v):
    
    for i in range(len(l)):
        if l[i]==v :
            pos=i
            break
    else:
        pos=-1
    
    return pos

        