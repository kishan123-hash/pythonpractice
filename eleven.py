def common_member(a, b):
    for i in a:
        for j in b:
            if i == j:
                return True
    return False
a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9, 10, 11, 6]

print(common_member(a, b))
