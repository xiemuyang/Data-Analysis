# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:51:41 2020

@author: XieSonghang
"""


import numpy as np

persontype=np.dtype({'names':["姓名","语文","数学","英语"],'formats':["U32","i","i","i"]})
peoples=np.array([("张飞",68,65,30),("关羽",95,76,98),("刘备",98,86,88),("典韦",90,88,77),("许褚",80,90,90)],dtype=persontype)

#print(peoples)
chinese=peoples["语文"]
math=peoples["数学"]
english=peoples["英语"]
print('语文平均分:%s 语文max:%s 语文min:%s 语文方差:%s 语文标准差:%s' %(np.mean(chinese),np.max(chinese),np.min(chinese),np.var(chinese),np.std(chinese)))
#print(np.mean(math))
#print(np.mean(english))
print(sorted(peoples,key= lambda x:x[1]+x[2]+x[3],reverse=True))