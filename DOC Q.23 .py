my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
sort_the_list=[]
for i in my_dict:
    sort_the_list.append(my_dict[i])
for j in range(0,len(sort_the_list)):
    for k in range(0,len(sort_the_list)):
        if sort_the_list[j]>sort_the_list[k]:
            sort_the_list[j],sort_the_list[k]=sort_the_list[k],sort_the_list[j]         
a=[]
for l in my_dict:
    if my_dict[l]==sort_the_list[0] or my_dict[l]==sort_the_list[1] or my_dict[l]==sort_the_list[2]:
        a.append({l:my_dict[l]})
print(a)