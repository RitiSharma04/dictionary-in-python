##. Write a Python program to combine values in python list of dictionaries. Go to the editor
##Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
##Expected Output: Counter({'item1': 1150, 'item2': 300})


dic= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

d={}
for i in dic:
        if i['item'] not in d:
            d[i['item']]=i['amount']
        else:
            d[i['item']]+=i['amount']
print(d)                