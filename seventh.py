a=[1,2,1,3,5,2,3,8,9,7,6]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)