# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import pandas as pd
data={'trans':[2,2,2,4],'item':['xie','song','nong','you']}
data=pd.DataFrame(data)
data2=data.set_index('trans')['item']
#print(data2)
transactions = []
id_=[]
temp_index=0
for i, v in data2.items():
    id_.append(i)
    if i!=temp_index:
        temp_set=set()
        temp_index=i
        temp_set.add(v)
        transactions.append(temp_set)
    else:
        temp_set.add(v) 
print(transactions)
print(id_)