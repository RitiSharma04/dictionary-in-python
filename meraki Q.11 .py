my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[]
for  i in my_dict:
    a.append(my_dict[i])      
b=[] 
for j in range(0,len(a)):
    for k in range(j+1,len(a)):
        if a[j]>=a[k]:
            a[j],a[k]=a[k],a[j]
b.append(a[-3])   
b.append(a[-2])
b.append(a[-1])
print(b)        


            
