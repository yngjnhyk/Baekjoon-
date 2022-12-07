n = int(input())
numbers = list(map(int, input().split()))
dp = [0] * n
dp[0] = numbers[0]
for i in range(1, n):
    arr = []
    for j in range(i - 1, -1, -1):
        if numbers[i] > numbers[j]:
            arr.append(dp[j])
    if not arr:
        dp[i] = numbers[i]
    else:
        dp[i] = numbers[i] + max(arr)
print(max(dp))
