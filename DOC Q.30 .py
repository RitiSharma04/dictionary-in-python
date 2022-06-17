dic={'S 001': ['Math', 'Science'], 'S002': ['Math','English']}
dic1={}
for i in dic:
    ##First we use split() function to return a list of the words in the string, using sep as the delimiter string.
    #  Then, we use join() to concatenate the iterable.
    dic1.update({ "".join(i.split()):dic[i]})
print(dic1)    


    
