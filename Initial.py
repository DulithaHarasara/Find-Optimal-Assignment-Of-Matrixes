import math
import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
from collections import Counter

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

dic_df_value = {}
for key,df in valueInDataFrames.items():
    df_alpha_value = []

    emptyList = []
    for alphaValue in alpha:

        numberList = []

        if alphaValue < 0.5:
            list1 = []
            list2 = []

            for i in df['a'],df['b'],df['c']:
                list1.append(i.tolist())

            numCount = 0
        
            for i in range(n**2):

                list3 = []

                for K in list1:
                    list3.append(K[numCount])

                x = formulaFunctionLowerThan5(alphaValue,list3[0],list3[1],list3[2])
                numberList.append(x)

                numCount = numCount + 1
            
            df_alpha_value.append(numberList)

        else:
            list1 = []
            list2 = []

            for i in df['a'],df['b'],df['c']:
                list1.append(i.tolist())

            numCount = 0
        
            for i in range(n**2):

                list3 = []

                for K in list1:
                    list3.append(K[numCount])

                x = formulaFunctionLowerThan5(alphaValue,list3[0],list3[1],list3[2])
                numberList.append(x)

                numCount = numCount + 1

            df_alpha_value.append(numberList)

        dic_df_value[f"{key}"] = df_alpha_value

print(dic_df_value)
dict_cost_matrix = {}
for key,df in dic_df_value.items():
    df_row_col = []
    for value in df:
        value = np.array(value)
        
        rowCol = []
        row_ind, col_ind = linear_sum_assignment(value.reshape(n,n))
        rowCol.append(row_ind)
        rowCol.append(col_ind)
        df_row_col.append(rowCol)
    dict_cost_matrix[f"df_{key}"] = df_row_col

dic_optimal_assignment = {}
for key,value in dict_cost_matrix.items():
    list_optimal_assignment = []
    for k in value:
        #print("Optimal Assignment:", list(zip(k[0], k[1])))
        list_optimal_assignment.append(list(zip(k[0], k[1])))

    dic_optimal_assignment[f"{key}"] = list_optimal_assignment


for key,value in dic_optimal_assignment.items():
    element_counts = Counter(tuple(item) for item in value)

    for element, count in element_counts.items():
        if count > 1:
            print(f"{list(element)} = {count}")

    print(key,":______________________________________________________________________________________________________")

x = {}
cost_value_step = ""
cost_value = 0
for key,value in dic_df_value.items():
    countListCostMetrix = 0
    listy = []
    for i in value:
        # print(dict_cost_matrix[key])
        x = np.array(i).reshape(n,n)[list_optimal_assignment[countListCostMetrix][0],list_optimal_assignment[countListCostMetrix][1]].sum()
        listy.append(x)
        countListCostMetrix = countListCostMetrix + 1
    
    #x[f"df_{key}"] = listy
    cost_value_step = cost_value_step + f"({listy[0]}) "
    cost_value = cost_value + listy[0]

# print(list_optimal_assignment[""])
print(f"{cost_value_step}")

print(f"average minimum cost = {cost_value/100} ")