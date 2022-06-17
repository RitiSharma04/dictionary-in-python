a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dic={}
for i in a:
    for j in range(0,len(a[i])):
        if a[i][0]==a[i+1][0]:
            dic.update({a[i][0]:a[i][1]})
print(dic)            



