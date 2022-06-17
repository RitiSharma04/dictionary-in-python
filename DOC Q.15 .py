dict1={"name":"Raju", "marks":56,"riti":5,"tanu":6}
dic={}
for i in dict1:
    if i!="name":
       dic.update({i:dict1[i]})
print(dic)         
