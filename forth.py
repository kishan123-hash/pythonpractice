a=[2,4,6,1,5,8,7,10]
min=a[0]
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
print(min)