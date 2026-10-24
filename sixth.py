
a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for j in range(len(a)):
    for i in range(len(a)-1):
        if a[i][-1] > a[i+1][-1]:
            a[i], a[i+1] = a[i+1], a[i]

print(a)
