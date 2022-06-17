my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
list_of_values=list(my_dict.values())
for i in range(0,len(list_of_values)):
    for j in range(0,len(list_of_values)):
        if list_of_values[i]>list_of_values[j]:
           list_of_values[i],list_of_values[j]=list_of_values[j],list_of_values[i]      
print(list_of_values)
for k in range(0,3):      
    for l in my_dict:
        if my_dict[l]==list_of_values[k]:
            print({l:my_dict[l]})
