##Write a Python program to map two lists into a dictionary.
dic={}
len_of_dic=int(input("enter the len:-"))
for i in range(0,len_of_dic):
    key=input("enter the key:-")
    value=int(input("enter the value:-"))
    dic.update({key:value})
print(dic)    

