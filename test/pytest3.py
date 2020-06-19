#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
#import xlrd
from pandas import Series,DataFrame


import pandas as pd
import numpy as np

orders = pd.read_excel("D:/info.xlsx")
#orders.groupby(['填报人','金额']).sum()

groups=orders.groupby(['填报人'])



s=groups['金额'].sum()
c=groups['金额'].sum()

pt2=pd.DataFrame({'金额':s})

# 获取PM列的值
pmList = orders[['费用类型']].values.T.tolist()[:][0]
print(pmList)

# 排除重复值
# pmList = list(set(pmList))
# sum_list = [['PM', 'Offer']]
# for pm in pmList:
#     temp = []
#     dfByPM = orders.loc[orders['费用类型'] == pm]
#     temp.append(pm)
#     for col in dfByPM.columns:
#         if col == '金额':
#             sumValue = dfByPM[col].sum()  # 计数指定列的和
#             temp.append(sumValue)
#     sum_list.append(temp)
#
# print(sum_list)




# print(pt2.append(sum_list))
# pt2 = pt2.append(sum_list)
# 定义ID为索引

# 生成excel文件output.xlsx，并保存到对应的位置。注意如果直接放到C盘可能会有问题！
pt2.to_excel('D:/按人员费用分类.xlsx')

