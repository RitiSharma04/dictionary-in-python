my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in my_dict:
    print(i,end=" ")
for j in my_dict.values():
    print()
    for k in range(0,len(j)):
        print(j[k],end=" ")
