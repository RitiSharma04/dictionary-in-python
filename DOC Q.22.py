dic = {'1':['a','b'], '2':['c','d']}   
list_of_values=list(dic.values())
# print(list_of_values)
for j in list_of_values[0]:
        for k in list_of_values[1]:
            print(j,k)

