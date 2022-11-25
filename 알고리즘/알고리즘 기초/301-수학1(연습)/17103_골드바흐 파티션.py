array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for j in range(i * i, 1000001, i):
            array[j] = False

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    cnt = 0
    for i in range(2, n // 2 + 1):
        if array[i] and array[n - i]:
            cnt += 1
    print(cnt)
