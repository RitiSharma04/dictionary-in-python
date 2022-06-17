Sample_data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
'item5': 24}
a=[]
for i in Sample_data:
    a.append(Sample_data[i])
for j in range(0,len(a)):
    for i in range(0,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
for k in range(0,3):                   
    for l in Sample_data:
        if Sample_data[l]==a[k]:
            print({l:Sample_data[l]})


