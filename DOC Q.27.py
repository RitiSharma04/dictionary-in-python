student = [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
a=input("enter the key:-")
for i in range(0,len(student)):
    dic={}
    for  j in student[i]:
        dic.update({a:student[i][a]})
        if a in dic:
            dic[a]+=student[i][a]
print(dic)        