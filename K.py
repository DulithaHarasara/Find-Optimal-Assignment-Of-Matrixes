import math
import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt

n = int(input("Size of the matrix: "))
emptyList = []

# load data
data = pd.read_csv('NumberList-2.csv')

df = pd.DataFrame(data)

a = np.array(df.iloc[:,0].values).flatten()
c = np.array(df.iloc[:,1].values).flatten()
b = np.array(df.iloc[:,2].values).flatten()
#alpha=np.array(df.iloc[:,3].values).flatten()

abcValueList = [a,b,c]

alpha = [0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.3,0.325,
         0.35,0.375, 0.4,0.425, 0.45,0.475, 0.5,0.525,0.55,0.575,0.6,0.625,
         0.65,0.675,0.7,0.725,0.75,0.775,0.8,0.825,0.85,0.875,0.90,0.925,
         0.95,0.975]


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

for alphaValue in alpha:

    numberList = [] 

    if alphaValue < 0.5:

        list1 = []
        list2 = []

        for j in a,b,c:
            list1.append(j.tolist())

        numCount = 0
    
        for i in range(n**2):

            list3 = []

            for K in list1:
                list3.append(K[numCount])

            x = formulaFunctionLowerThan5(alphaValue,list3[0],list3[1],list3[2])
            numberList.append(x)

            numCount = numCount + 1

        emptyList.append(numberList)

            

    else:
        numberList = [] 

        list1 = []
        list2 = []

        for j in a,b,c:
            list1.append(j.tolist())

        numCount = 0

        for i in range(n**2):

            list3 = []

            for K in list1:
                list3.append(K[numCount])

            x = formulaFunctionGraterThan5(alphaValue,list3[0],list3[1],list3[2])
            numberList.append(x)

            numCount = numCount + 1
        
        emptyList.append(numberList)
       

emptyListCount = 1

for i in emptyList:
    print("List:",emptyListCount)
    print(i)
    
    emptyListCount = emptyListCount + 1
    
print(type(emptyList))
    
cost_matrix = np.array(emptyList)
#print(cost_matrix)
#Optimization part

listCostMetrix = []

for i in cost_matrix:
    rowCol = []
    row_ind, col_ind = linear_sum_assignment(i.reshape(n,n))
    rowCol.append(row_ind)
    rowCol.append(col_ind)
    listCostMetrix.append(rowCol)
    
        

for k in listCostMetrix:
    print("Optimal Assignment:", list(zip(k[0], k[1])))

# Calculate the minimum total cost based on the optimal assignment

countListCostMetrix = 0

  
listy = []      
for i in cost_matrix:
    x = i.reshape(n,n)[listCostMetrix[countListCostMetrix][0],listCostMetrix[countListCostMetrix][1]].sum()
    listy.append(x)
    countListCostMetrix = countListCostMetrix + 1

print(listy)

#######################################################################################3
x=alpha
#x = np.arange(0, 1.05, 0.05)
y=listy
plt.plot(alpha,listy,"o",linestyle='-')
plt.xlabel(' Alpha value', fontsize=16)
plt.ylabel('Uncertain value', fontsize=16)
plt.grid(True)
plt.show()
#plt.title('The graph of Uncertain value vs alpha',fontsize=18)