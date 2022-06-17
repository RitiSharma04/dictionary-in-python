student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
for i in student:
    count=0
    for j in i :
        if type(i[j])!=str:
             count=count+i[j]
    print(count)    
