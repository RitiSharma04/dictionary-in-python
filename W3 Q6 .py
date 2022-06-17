dic={}
len_of_dic=int(input("enter the num:-"))
for i in range(0,len_of_dic):
    key=input("enter the num:-")
    value=int(input("enter the value:-"))
    dic.update({key:value})
print(dic)    