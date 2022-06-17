dic='w3resource'
d={}
for i in dic:
    c=0
    for j in dic:
        if i==j:
            c=c+1
        d.update({i:c})     
print(d)       
