#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
#import xlrd
from pandas import Series,DataFrame
import pandas as pd
import numpy as np

orders = pd.read_excel("D:/info.xlsx")


in_str = input('填报人:')
orders = orders[orders['填报人'] == in_str]
#
# in_str = input('费用类型:')
# orders = orders[orders['费用类型'] == in_str]

pt1 = orders.pivot_table(index='费用类型',columns='填报人',values='金额',aggfunc=np.sum, margins=True ,margins_name='合计')

print(pt1)
# 定义ID为索引

# 生成excel文件output.xlsx，并保存到对应的位置。注意如果直接放到C盘可能会有问题！


pt1.to_excel('D:/按费用类型分类.xlsx',sheet_name="sdfsda")

