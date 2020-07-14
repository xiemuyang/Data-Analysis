# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:32:49 2020

@author: XieSonghang
"""
def f1():
    sum=0
    for i in range(2,101,2):
        sum=sum+i   
    print(sum)

def f2():
    sum=0
    i=2
    while i<101:
        sum=sum+i  
        i=i+2
    print(sum)

f1()
f2()