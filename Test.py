import math

from numpy import array

dict_1 = {
    "df_1":{"a":[1,2,3],"b":[2,5,6],"c":[3,4,5]},
    "df_2":{"a":[13,25,34],"b":[23,5,6],"c":[33,43,5]}
}

print(dict_1["df_1"]["a"])

count = 1
for key,df in dict_1.items():
        list1 = []

        a = df["a"]
        b = df["b"]
        c = df["c"]
        # list1.append(a)
        # list1.append(b)
        # list1.append(c)

        print(list1)


dict_2 = {
    "df_1":[[1,2,3],[2,3,4],[2,5,6]],
    "df_2":[[1,2,5],[2,3,5],[2,5,6]],
}

print((dict_2["df_1"])[0][1])

# for key,df in dict_2.items():[]
#         print(df)

# list11 = []
# a = [1,2,3]
# b = [4,5,6]
# c = [3,5,6]

# for i in a,b,c:
#     list11.append(i)

# print(list11)

# # def formulaFunctionGraterThan5(alpha,a,b,c):
# #     expression = (b - a) * (b - c) * (1 - alpha)
# #     if expression >= 0:
# #         formuala = b - math.sqrt(expression)
# #     else:
# #         raise ValueError("The expression inside the square root is negative.")
# #     return formula

# # print(formulaFunctionGraterThan5(0.025,1.6009065147495714,5.793815960957356,8.178336410730083))

# # print(math.sqrt(1.343434))

# list122 = []
# list122.append(1)
# list122.append(2)
# list122.append(3)

# print(list122)

# x = {'a': array([2.38596845, 2.1415868 , 2.62259447, 0.17907544]), 'c': array([6.27719733, 6.41817814, 5.12007298, 5.09474284]), 'b': array([8.15835903, 9.29268685, 8.81190438, 8.73049817])}

# list1234 = []
# for i in x['a'],x['c'],x['b']:
#        list1234.append(i.tolist())

# print(list1234)