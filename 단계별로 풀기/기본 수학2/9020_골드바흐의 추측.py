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

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    for a in range(n // 2, 0, -1):
        if sosu(a) and sosu(n - a):
            print(a, n - a)
            break
            