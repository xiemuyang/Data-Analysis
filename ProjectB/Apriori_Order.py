# -*- coding: utf-8 -*-
"""
使用Apriori算法，挖掘订单中的频繁项集及关联规则

"""

import pandas as pd
import time

# 数据加载
data = pd.read_csv('./订单表.csv',encoding='gbk')
# 筛选所需字段
train=data[['客户ID','订单日期','产品ID']]
#print(train.head())

# 采用efficient_apriori工具包
def rule1():
    from efficient_apriori import apriori
    start = time.time()
    transactions= []
    # 基于客户ID和订单日期字段汇总订单item
    for name, group in train.groupby(['客户ID','订单日期']):
        temp_set=set(group['产品ID'])
        transactions.append(temp_set)
    print(transactions[:10])
    # 挖掘频繁项集和频繁规则
    itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.5)
    print('频繁项集：', itemsets)
    print('关联规则：', rules)
    end = time.time()
    print("用时：", end-start)

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
# 采用mlxtend.frequent_patterns工具包
def rule2():
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules
    pd.options.display.max_columns=100
    start = time.time()
    temp_df=train.groupby(['客户ID','订单日期','产品ID'])['产品ID'].count().unstack().reset_index().fillna(0)
    temp_df['ID']=range(len(temp_df))
    hot_encoded_df=temp_df.drop(['客户ID','订单日期'],1).set_index('ID')
    #print(hot_encoded_df.head())
    hot_encoded_df=hot_encoded_df.applymap(encode_units)
    frequent_itemsets = apriori(hot_encoded_df, min_support=0.02, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
    print("频繁项集：", frequent_itemsets)
    print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.5) ])
    #print(rules['confidence'])
    end = time.time()
    print("用时：", end-start)

rule1()
print('-'*100)
rule2()
