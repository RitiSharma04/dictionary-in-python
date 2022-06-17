dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
a,b=dic.values()     
list=[]          
for i in  range(len(a)):
    d={}
    for j in dic:
        d.update({j:dic[j][i]})
    list.append(d)
print(list)
