##Write a Python program to print all unique values in a dictionary. Go to the editor
##Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VI":"S005"}, {"V":"S009"},{"VIII":"S007"}]
dic= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VI":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d=[]
for i in dic:
    for j in i:
        if i[j] not in d:
            d.append(i[j])
print(d)            


