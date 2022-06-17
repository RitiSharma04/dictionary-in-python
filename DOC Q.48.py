dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dic_of_len_of_values={}
for i in dic:
    dic_of_len_of_values.update({dic[i]:len(dic[i])})
print(dic_of_len_of_values)    