import math

N, S = map(int, input().split())
n = list(map(int, input().split()))

distanse = []
for i in n:
    distanse.append(abs(S - i))

ans = distanse[0]
for i in range(1, N):
    ans = math.gcd(distanse[i], ans)
print(ans)
