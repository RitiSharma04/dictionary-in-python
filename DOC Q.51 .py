dic={'V': [1, 9, 11, 11], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dic1={}
for i  in dic:
    a=[]
    for j in dic[i]:
            if j%2==0:
                a.append(j) 
            dic1.update({i:a})
print(dic1)            