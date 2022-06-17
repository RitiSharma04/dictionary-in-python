my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in my_dict:
    print(i,end=" ")    
li=list(my_dict.values())
for j in range(0,len(li)):
    print()
    for k in range(0,len(li)):
            print(li[j][k],end="  ")
 
