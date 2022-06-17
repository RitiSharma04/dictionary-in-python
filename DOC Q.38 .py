dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
dic1={}
for i in dic:
    if dic[i]!=None:
       dic1.update({i:dic[i]})
print(dic1)       