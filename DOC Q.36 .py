dictionary={'key1': 1, 'key2': 3, 'key3': 2}
dictionary2={'key1': 1, 'key2': 2}
for i in dictionary:
    for j in dictionary2:
        if {i:dictionary[i]}=={j:dictionary2[j]}:
            print({i:dictionary[i]})