a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
b=[]
for i in range(len(a)-1,-1,-1):
    if i in (0,4,5):
        continue
    else:
        b.append(a[i])
print(b)