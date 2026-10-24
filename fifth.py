a=['abc', 'xyz', 'aba', '1221']
count=0
for i in range(len(a)):
    if len(a[i])>=2 and a[i][0]==a[i][-1]:
        count+=1
print(count)