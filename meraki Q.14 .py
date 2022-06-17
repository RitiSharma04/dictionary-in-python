# dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a={b:c for b,c in sorted(dic.items())}    
# print(a)     
# d={b:c for  b,c in sorted(dic.items(),key=lambda v:v[1])}
# print(d)

# num = {'physics': 80, 'math': 90, 'chemistry': 86,'r':34,"f":93,"t":5}
# num1={}
# c=[]
# for i in num:
#     c.append(num[i])        
# for k in range(len(c)):         
#     for j in range(k+1,len(c)):
#             if c[k]>c[j]:
#                 c[k],c[j]=c[j],c[k]                  
# for n in range(0,len(c)):
#     for l in num:
#                     if c[n]==num[l]:
#                                 num1.update({l:num[l]})
# print(num1)


num = {'physics': 80, 'math': 90, 'chemistry': 86,'r':34,"f":93,"t":5}
a=[]
num1={}
for i in num:
    a.append(i)    
a.sort()
for j in range(0,len(a)):
    for k in num:
        if a[j]==k:
            num1.update({k:num[k]})
print(num1)            
             
       
