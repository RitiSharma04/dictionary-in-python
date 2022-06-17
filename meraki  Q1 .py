dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d={}
for i in (dic1,dic2,dic3):
    d.update(i)
for i in d:
    if i in dic1:
        if i in dic2:
            d.update({i:dic1[i]+dic2[i]}) 
print(d)               
         