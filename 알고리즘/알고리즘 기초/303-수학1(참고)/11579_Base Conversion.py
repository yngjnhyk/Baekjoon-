import math

A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
ten = 0

for i in range(m):
    ten += arr[m - i - 1] * A ** i

ans = ""

while ten:
    ans = " " + ans
    ans = str(ten % B) + ans
    ten //= B

print(ans)