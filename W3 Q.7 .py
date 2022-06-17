dic={}
key=int(input("enter the key:-"))
for i in range(1,key):
    dic.update({i:i*i})
print(dic)    