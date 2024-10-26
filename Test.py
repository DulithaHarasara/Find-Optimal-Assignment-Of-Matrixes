import math

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

print((dict_2["df_1"])[0])

for key,df in dict_2.items():
        print(df)
         
