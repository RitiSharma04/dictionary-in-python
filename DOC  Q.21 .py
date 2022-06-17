Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
list_of_values=[]
for i in range(0,len(Sample_Data)):
    for j in Sample_Data[i]:
        if Sample_Data[i][j] not in list_of_values:
            list_of_values.append(Sample_Data[i][j])
print(list_of_values)        