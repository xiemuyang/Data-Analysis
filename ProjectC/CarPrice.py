# -*- coding: utf-8 -*-
"""
数据包括了205款车的26个字段
对该汽车数据进行聚类分析，并找到vokswagen汽车的相应竞品
"""

# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

# 数据加载
data = pd.read_csv('CarPrice_Assignment.csv', encoding='gbk')
train_x = data[["symboling","fueltype", "aspiration","doornumber","carbody","drivewheel","enginelocation","wheelbase",
                "carlength","carwidth","carheight","curbweight","enginetype","cylindernumber","enginesize","fuelsystem",
                "boreratio","stroke","compressionratio","horsepower","peakrpm","citympg","highwaympg","price"]]

# LabelEncoder对Categorical类型数据处理成连续数据
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
catolist=["fueltype", "aspiration","doornumber","carbody","drivewheel","enginelocation","enginetype","cylindernumber","fuelsystem"]
for i in catolist:
    train_x[i] = le.fit_transform(train_x[i])

# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
#pd.DataFrame(train_x).to_csv('temp.csv', index=False)

# 使用KMeans聚类
kmeans = KMeans(n_clusters=15)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:'cluster'},axis=1,inplace=True)
# 将结果导出到CSV文件中
#result.to_csv("Cluster_Result.csv",index=False,encoding='gbk')

# 寻找VW竞品车型
set_vw=set(result[result.CarName.str.contains('volkswagen')].cluster)
print (set_vw)
rival=result[result.cluster.isin(list(set_vw))].sort_values(by='cluster')
print (rival.head())

# 将结果导出到CSV文件中
rival.to_csv("Competitor_Car.csv",index=False,encoding='gbk')

"""
# K-Means 手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse = []
for k in range(1, 31):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(train_x)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 31)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()
"""