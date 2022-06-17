# a="MISSISSIPPI" 
# s={}
# i=0
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     if c>1:
#         if a[i] not in s:
#             s.update({a[i]:c})
#     else:
#         s.update({a[i]:c})
#     i=i+1
# print(s)        

a="MISSISSIPPI" 
b={}
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c=c+1
    b.update({a[i]:c})   
print(b)