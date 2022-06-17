a={"a":2,"b":7,"c":8,"d":1,"e":45,"f":6}
dic={}
li=list(a.values())
li.sort()
for j in li:
    for i in a:
        if j==a[i]:
            dic.update({i:a[i]})
print(dic)
    
    
   