import math

test_case = int(input())

for i in range(test_case):
    numbers = list(map(int, input().split()))
    total = 0
    for j in range(1, len(numbers)):
        for k in range(j+1, len(numbers)):
            sum += math.gcd(numbers[j], numbers[k])

    print(total)

