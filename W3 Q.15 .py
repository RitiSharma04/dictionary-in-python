##. Write a Python program to get the maximum and minimum value in a dictionary.
dic={"a":8,"o":5,"e":5,"y":4,"g":9}
li=list(dic.values())
li.sort()
for i in dic:
    if li[-1]==dic[i]:
        print("Max",{i:dic[i]})
    elif li[0]==dic[i]:
        print("Min",{i:dic[i]})

