dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['ZacarySimon']}
a=[]
dic1={}
for i in dic:
    dic1.update({i:dic[i][0]})
a.append(dic1)
print(a)