dic=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
dic1={}
for i in dic:
    for j in range(0,len(i)-1):
        dic1.update({i[0]:[i[1],i[2]]})     
print(dic1)        
