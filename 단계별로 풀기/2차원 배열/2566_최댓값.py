num = 0
col = 0
row = 0
for i in range(9):
    line = list(map(int, input().split()))
    if max(line) > num:
        num = max(line)
        col = i
        row = line.index(num)
print(num)
print(col+1, row+1)
