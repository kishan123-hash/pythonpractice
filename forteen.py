a=[1,2,3,4,5,6,7,8,9]
b=[]
for i in a:
    if i not in b and i%2!=0:
        b.append(i)
print(b)
