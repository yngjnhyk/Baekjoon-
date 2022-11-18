N, M = map(int, input().split())
lst = list(map(int, input().split()))
n_list = []
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum = lst[i] + lst[j] + lst[k]
            if sum > M:
                continue
            else:
                n_list.append(sum)
print(max(n_list))
