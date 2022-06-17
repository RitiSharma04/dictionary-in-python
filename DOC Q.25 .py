Sample_string = 'w3resource'
dic={}
for i in Sample_string:
    count=0
    for j in Sample_string:
        if i==j:
            count=count+1
    dic.update({i:count})   
print(dic)     
