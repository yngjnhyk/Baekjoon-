n = int(input())
numbers = list(map(int, input().split()))
dpp = [0] * n
dpm = [0] * n
dpb = [0] * n

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j] and dpp[i] < dpp[j]:
            dpp[i] = dpp[j]
    dpp[i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if numbers[i] > numbers[j] and dpm[i] < dpm[j]:
            dpm[i] = dpm[j]
    dpm[i] += 1
for i in range(n):
    dpb[i] = dpp[i] + dpm[i] - 1
print(max(dpb))
