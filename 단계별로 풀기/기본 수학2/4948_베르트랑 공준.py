import math

def sosu(num):
    a = int(math.sqrt(num))
    if num == 1:
        return False
    else:
        for i in range(2, a+1):
            if num % i == 0:
                return False
        return True

Num_list = list(range(2,246912))
sosu_list = []

for i in Num_list:
    if sosu(i):
         sosu_list.append(i)

while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in sosu_list:
        if N < i <= N*2:
            cnt += 1
    print(cnt)
