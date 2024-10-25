import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt

dataframe_dic = {}
valueInDataFrames = {}

n = int(input("Size of the matrix: "))

# for df in range(10):
#     dataframe_dic[f"df_{df+1}"] = pd.DataFrame({'A': [1, 2, df],'B': [4, 5, df],'C': [4, 5, df]})

for df in range(100):
    rowList = []

    for i in range(n*n):
        a = np.random.uniform(np.finfo(float).eps,4 - np.finfo(float).eps)
        b = np.random.uniform(4,7 - np.finfo(float).eps)
        c = np.random.uniform(7,11 - np.finfo(float).eps)
        new_row = {"A": a,"B": b,"C": c}
        rowList.append(new_row)

    dataframe_dic[f"df_{df+1}"] = pd.DataFrame(rowList)

dataFrameCount = 1
for df in dataframe_dic:
    a = np.array(dataframe_dic[df].iloc[:,0].values)
    b = np.array(dataframe_dic[df].iloc[:,1].values)
    c = np.array(dataframe_dic[df].iloc[:,2].values)

    valueDic = {"a":a,"b":b,"c":c}
    valueInDataFrames[f"df_{dataframe_dic}"] = valueDic
    dataFrameCount = dataFrameCount + 1

print(valueInDataFrames)




