dic=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
dic1={}
for i in dic:
    for j in i:
         dic[j]=int(i[j])         
print(dic1)  
