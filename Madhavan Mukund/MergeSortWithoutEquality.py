# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:10:41 2018

@author: soumy
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:12:51 2018

@author: soumy
"""

def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    print('merge called')
    while i+j < m+n:
        if(i==m):
            c.append(b[j])
            print ("C when A finished=",c)
            j=j+1
        elif(j==n):
            c.append(a[i])
            print ("C when B finished=",c)
            i=i+1
        elif(a[i]<=b[j]):
            c.append(a[i])
            print ("C when A lesser=",c)
            i=i+1
        elif(b[j]<a[i]):
            c.append(b[j])
            print ("C when B lesser=",c)
            j=j+1
       
    return c

def mergesort(a,left, right):
    print('mergesort called')
    print('a in mergesort',a[left:right])
    if right-left<=1:
        return(a[left:right])
    if(right-left>1):
        mid=(left+right)//2
        L=mergesort(a,left, mid)
        print('L=',L,'  ',mid)
        R=mergesort(a,mid,right)
        print('R=',R,'  ',mid)
        return merge(L,R)
                
            
            
            
        
        