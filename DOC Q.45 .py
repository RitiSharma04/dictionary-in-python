dic=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color':
'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
value_you_want_to_remove=input("enter the value")
for i in dic:
    for j in i:
        if value_you_want_to_remove  in i[j]:
            i.pop(value_you_want_to_remove) 
print()            