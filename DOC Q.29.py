l={"riti":3,"zen":4,"bulbul":6,"priti":10}
a=list(l.keys())
a.sort()
dic={}
for j in a:
    for i in l:
        if j==i:
           dic.update({i:l[i]})
print(dic)           
