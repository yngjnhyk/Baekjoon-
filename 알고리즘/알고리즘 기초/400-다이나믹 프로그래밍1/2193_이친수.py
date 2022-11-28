N = int(input())
prinary_list = [0, 1, 1]
for i in range(3,91):
    prinary_list.append(prinary_list[i-2] + prinary_list[i-1])

print(prinary_list[N])

