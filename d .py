# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
# print(type(Employee))    
# print("printing Employee data .... ")    
# print(Employee)    
# print("Enter the details of the new employee....");    
# Employee["Name"] = input("Name: ");    
# Employee["Age"] = int(input("Age: "));    
# Employee["salary"] = int(input("Salary: "));    
# Employee["Company"] = input("Company:");    
# Employee["education"]=input()
# print("printing the new data");    
# print(Employee)    


# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
# for x in Employee:    
#         print(x)  


# dic={"ball":"red","rani":4,"wickets":8,"riti":"green","bat":3}
# a=input("enter the kye:-")
# if a in dic :
#         dic.pop(a)  
# else:
#     c=input("enter the num:-")
#     dic.update({a:c})
# print(dic) 


# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print(len(fruit))
# print(fruit)





# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(len(Details)) 

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# print(my_dict)
# # 
# # 
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print(sum)
# print(my_dict)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates['jars']))



# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)

# details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org",}

# print(details["name"])
# print(details["email"])
# print(details["age"])

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1:
#     sum=sum+dict1[i]
# print(sum)


# c={}
# for i in range(1,16):
#    c.update({i:i*i})
# print(c)


# a={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56,'python':20,"gaurav":300,'dev':34,"karan":43}

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)


# clear ()

# a={"name":"riti","age":18}
# a.clear()
# print(a)

## copy()

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# b=a.copy()
# # b=a
# del b["a"]
# print(b)
# print(a)


## fromkeys(seq[,v])=Returns a new dictionary with keys from seq and value equal to v (defaults to None).

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# b="riti"
# values=a.fromkeys(a,b)
# print(values)

## get(key[,d]) =Returns the value of the key. If the key does not exist, returns d (defaults to None).


# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# print(a.get("a")[2])
# print(type(a.get("a")))


# person = {'name': 'Phill', 'age': 22}
# print('Name: ', person.get('name'))
# print('Age: ', person.get('age'))
# # value is not provided
# print('Salary: ', person.get('salary'))
# # value is provided
# print('Salary: ', person.get('salary', 0.0))

## items()

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# print(a.items())

## keys()


# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# print(a.keys())


##  pop()

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# b=a.pop("a")
# print(a)


## popitem()

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# for i in a:




###setdefault() =The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.

## if key is exist

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# r=a.setdefault("a")
# print(r)
# print(a)

## if key is not exist

# person = {'name': 'Phill'}
# ## key is not in the dictionary
# salary = person.setdefault('salary')
# print('person = ',person)
# print('salary = ',salary)
# # #key is not in the dictionary
# # #default_value is provided
# age = person.setdefault('name', 22)
# print('person = ',person)
# print('age = ',age)


## update()

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# a.update({"n":[8,0]})
# a["h"]=23
# print(a)


##update tuple()

# dictionary = {'x': 2}
# dictionary.update([('y', 3), ('z', 0)])
# print(dictionary)

## values()

# a={"a":[1,2,3,4],"b":[3,65,2,5],"c":(2,54,7,2),"d":2.3,"e":5}
# print(a.values())

## all() =The all() function returns True if all elements in the given iterable are true. If not, it returns False.


# boolean_list = ['True', 'True', 'True']
# # check if all elements are true
# result = all(boolean_list)
# print(result)


## any() =The any() function returns True if any element of an iterable is True. If not, it returns False.


# boolean_list = ['True', 'False', 'True']
# # check if any element is true
# result = any(boolean_list)
# print(result)


## sorted() =The sorted() function sorts the elements of a given iterable in a specific order (ascending or descending) and returns it as a list.
# a=[3,4,5,5,3]
# print(sorted(a))
# print(a.sort())

# dic={"math":95,"phy":72,"chem":61,"hindi":99,"sst":45}
# a=[]
# for i in dic:
#     a.append(dic[i])
# for j in range(0,len(a)):
#     for k in range(0,len(a)):
#         if a[j]>a[k]:
#             a[j],a[k]=a[k],a[j]
# for l in dic:
#     if dic[l]==a[0]:
#         print("m",{l:dic[l]}) 
#     if dic[l]==a[-1]:
#         print("min",{l:dic[l]})               


# a={1:"a",2:"b",1:"s",3:"d",2:"e"}
# d={}
# for i in a:
#     if i not in d.keys():
#         d.update({i:a[i]})
# print(d)     
# 
# a={}
# for i in range(0,3):
#     b={}
#     name=input("")
#     pro=input(" ")
#     age=int(input(" "))
#     salary=int(input(" "))
#     b.update({"pro":pro})   
#     b.update({"age":age})
#     b.update({"salery":salary})
#     a.update({name:b})
# print(a)