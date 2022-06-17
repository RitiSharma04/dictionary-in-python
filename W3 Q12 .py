##Write a Python program to remove a key from a dictionary. 
dic={"ball":"red","bat":4,"wickets":8,"stump":3}
a=input("enter the a:-")
if a in dic:
    dic.pop(a)
print(dic)    

