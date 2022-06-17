a={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 200, 'g': 57, 'h': 8, 'i': 100}
list_of_values=[]
for i in a:
    list_of_values.append(a[i])
for j in range(0,len(list_of_values)):
    for k in range(0,len(list_of_values)):
        if list_of_values[j]>list_of_values[k]:
            list_of_values[j],list_of_values[k]=list_of_values[k],list_of_values[j]  
list_of_key=[]
for l in range(0,5):
    for m in a:
       if list_of_values[l]==a[m]:
           list_of_key.append(m)     
print(list_of_key)
# max=0
# for i in a:
#     if a[i]>max:
#         max=a[i]
#         key=i
# print(key)        