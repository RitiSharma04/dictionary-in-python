## Write a Python program to sort a given dictionary by key.
dic={"r":2,"i":7,"t":3,"i":8,"s":2,"h":9,"a":7,"r":2,"m":0,"a":6}
li=list(dic.keys())
li.sort()
d={}
for  i in li:
    for j in dic:
        if i==j:
            d.update({j:dic[j]})
print(d)