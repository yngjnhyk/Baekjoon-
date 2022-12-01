test_case = int(input())

for i in range(test_case):
    numbers = []
    n = int(input())
    for k in range(2):
        numbers.append(list(map(int, input().split())))
    for j in range(1, n):
        if j == 1:
            numbers[0][j] += numbers[1][j - 1]
            numbers[1][j] += numbers[0][j - 1]
        else:
            numbers[0][j] += max(numbers[1][j - 1], numbers[1][j - 2])
            numbers[1][j] += max(numbers[0][j - 1], numbers[0][j - 2])
    print(max(numbers[0][n - 1], numbers[1][n - 1]))
