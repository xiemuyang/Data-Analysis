# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:50:41 2020

@author: XieSonghang
"""

import pandas as pd
#读取文件
result=pd.read_csv('car_complain.csv')
result=result.drop(columns=['problem']).join(result.problem.str.get_dummies(','))
#print(result.iloc[0])    
#品牌投诉总数
brand_complain=result.groupby('brand')['id'].agg(['count']).sort_values('count',ascending=False)
#print(brand_complain)

#品牌平均投诉数
brand_complain_average=result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand'])['count'].agg(['mean']).sort_values('mean',ascending=False)
print(brand_complain_average)
#写入excel文件
writer=pd.ExcelWriter('C:/Users/XieSonghang/car_analysis.xlsx')
result.to_excel(writer,sheet_name='sheet1')
writer.save()