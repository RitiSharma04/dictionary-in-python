dic={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196,15: 225}
list_of_values=[]
for i in dic:
    list_of_values.append(dic[i])  
b=list_of_values[0]    
for j in range(1,len(list_of_values)):
    if list_of_values[j]>b:
        b=list_of_values[j]
    if dic[i]==b:        
          print({i:dic[i]})