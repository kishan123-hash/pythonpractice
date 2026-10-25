b = []

for i in range(3):
    a = []
    for j in range(4):
        c = []
        for k in range(6):
            c.append("*")
        a.append(c)
    b.append(a)

print(b)