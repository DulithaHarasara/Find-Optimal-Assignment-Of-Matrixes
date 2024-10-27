import math
import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
from numpy import array

dataframe_dic = {}
valueInDataFrames = {}

alpha = [0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.3,0.325,
         0.35,0.375, 0.4,0.425, 0.45,0.475, 0.5,0.525,0.55,0.575,0.6,0.625,
         0.65,0.675,0.7,0.725,0.75,0.775,0.8,0.825,0.85,0.875,0.90,0.925,
         0.95,0.975]

emptyList = []

def formulaFunctionGraterThan5(alpha,a,b,c):
    formula = b - math.sqrt((b-a)*(b-c)*(1-alpha))
    return formula

def formulaFunctionLowerThan5(alpha,a,b,c):
    formula = a + math.sqrt(alpha * (b-a)*(c-a))
    return formula

def formula(alpha,a,b,c):
    u=(c-a)/(b-a)
    
    if 0< alpha and alpha < u:
        formulaFunctionLowerThan5(alpha, a, b, c)
    elif u <= alpha and alpha < 1:
        formulaFunctionGraterThan5(alpha, a, b, c)

# input size of the matrix
n = int(input("Size of the matrix: "))

# for df in range(10):
#     dataframe_dic[f"df_{df+1}"] = pd.DataFrame({'A': [1, 2, df],'B': [4, 5, df],'C': [4, 5, df]})

for df in range(100):
    rowList = []

    for i in range(n*n):
        a = np.random.uniform(np.finfo(float).eps,4 - np.finfo(float).eps)
        c = np.random.uniform(4,7 - np.finfo(float).eps)
        b = np.random.uniform(7,11 - np.finfo(float).eps)
        new_row = {"a": a,"c": c,"b": b}
        rowList.append(new_row)

    dataframe_dic[f"df_{df+1}"] = pd.DataFrame(rowList)

dataFrameCount = 1
for df in dataframe_dic:
    a = np.array(dataframe_dic[df].iloc[:,0].values)
    c = np.array(dataframe_dic[df].iloc[:,1].values)
    b = np.array(dataframe_dic[df].iloc[:,2].values)

    valueDic = {"a":a,"c":c,"b":b}
    valueInDataFrames[f"df_{dataFrameCount}"] = valueDic
    dataFrameCount = dataFrameCount + 1

for alphaValue in alpha:

    numberDict = {} 

    if alphaValue < 0.5:

        dict1 = {}
        list2 = []

        df_count = 1
        for key,df in valueInDataFrames.items():
            df_list = []
            b = df["b"]
            c = df["c"]
            a = df["a"]

            #print(df_list)

            #df_list.append([a,b,c])
            df_list.append(a)
            df_list.append(c)
            df_list.append(b)
           
            dict1[f"df_{df_count}"] = df_list
            df_count = df_count + 1

        numCount = 0

        df_number = 1
        for key,df in dict1.items():
            #print(df) #df = [[],[],[]]
            number_List = []
            numberCount = 0
            for i in range(n**2):
                dict3 = {}
                list3 = []

                #print(df)
                for k in df:
                    list3.append(k[numberCount]) 

                #print(alphaValue,list3[0],list3[1],list3[2])
                #print("--------------------------------------")
                x = formulaFunctionGraterThan5(alphaValue,list3[0],list3[2],list3[1])
                #print(x)
                number_List.append(x) 
                numberCount = numberCount + 1

            numberDict[f"df_{df_number}"] = number_List
            df_number = df_number + 1
        emptyList.append(numberDict)
    else:
        dict1 = {}
        list2 = []

        df_count = 1
        for key,df in valueInDataFrames.items():
            df_list = []
            b = df["b"]
            c = df["c"]
            a = df["a"]

            #print(df_list)

            #df_list.append([a,b,c])
            df_list.append(a)
            df_list.append(c)
            df_list.append(b)
           
            dict1[f"df_{df_count}"] = df_list
            df_count = df_count + 1

        numCount = 0

        df_number = 1
        for key,df in dict1.items():
            #print(df) #df = [[],[],[]]
            number_List = []
            numberCount = 0
            for i in range(n**2):
                dict3 = {}
                list3 = []

                #print(df)
                for k in df:
                    list3.append(k[numberCount]) 

                #print(alphaValue,list3[0],list3[1],list3[2])
                #print("--------------------------------------")
                x = formulaFunctionGraterThan5(alphaValue,list3[0],list3[2],list3[1])
                #print(x)
                number_List.append(x) 
                numberCount = numberCount + 1

            numberDict[f"df_{df_number}"] = number_List
            df_number = df_number + 1
        emptyList.append(numberDict)

dictCostMetrix = {}
dictPerDf = {}

# print(len(emptyList))
# print(emptyList[0])

for listItem in emptyList:
    rowCol = {}
    for key,df in listItem.items():
        print(key,":")
        print(df)
        row_ind,col_ind = linear_sum_assignment(np.array(df).reshape(n,n))
        rowCol.append(row_ind)
        rowCol.append(col_ind)

    print("-----------------")