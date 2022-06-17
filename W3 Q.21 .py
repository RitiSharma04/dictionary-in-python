##Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
##Sample data : {'1':['a','b'], '2':['c','d']}
##Expected Output:
##ac
##ad
##bc
##bd


dic={'1':['a','b'], '2':['c','d']}
list_of_values1=dic.get("1")
list_of_values2=dic.get("2")
for i in list_of_values1:
    for j in list_of_values2:
        print(i,j)
