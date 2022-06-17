len_of__dic=int(input("enter the len of dic:-"))
dic={}
i=0
while i<len_of__dic:
     list1=input("enter the key:-")
     list2=int(input("enter the valus:-"))
     dic.update({list1:list2})
     i=i+1
print(dic)     
