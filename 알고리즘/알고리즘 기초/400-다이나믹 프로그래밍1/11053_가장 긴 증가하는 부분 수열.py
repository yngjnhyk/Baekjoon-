numbers = int(input())
numbers_list = list(map(int, input().split()))
dp = [0] * (numbers + 1)
arr = []

for i in range(numbers):
    for j in range(i):
        if numbers_list[i] > numbers_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
