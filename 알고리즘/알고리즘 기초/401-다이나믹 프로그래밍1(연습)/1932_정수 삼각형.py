test_case = int(input())
arr = []

for _ in range(test_case):
    numbers = list(map(int, input().split()))
    arr.append(numbers)
k = 2
for i in range(1, test_case):
    for j in range(k):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif i == j:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
    k += 1
print(max(arr[test_case - 1]))
