#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
#import xlrd
from pandas import Series,DataFrame


import pandas as pd
import numpy as np

orders1 = pd.read_excel("D:/info.xlsx")
pt1 = orders1.pivot_table(index='费用类型',values='金额',aggfunc=np.sum, margins=True ,margins_name='合计')
pt1.to_excel('D:/按项目费用分类.xlsx',sheet_name="按项目费用分类")






