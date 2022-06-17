dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=[]
c={}
for i in dictionary:
    a.append(dictionary[i])       
for j in range(len(a)):
    for k in range(len(a)):
        if a[j]<a[k]:
            a[j],a[k]=a[k],a[j]            
for m in range(len(a)):
    for l in dictionary:
        if dictionary[l]==a[m]:
                c.update({l:dictionary[l]})
print(c)                

        
