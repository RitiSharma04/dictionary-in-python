list1=['S001', 'S002', 'S003', 'S004']
list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3=[85, 98, 89, 92]
values=zip(list2,list3)
dic={}
for i in range(0,len(list1)):
        dic[i]=values[i]
print(dic)        