N, K = map(int, input().split())
N_list = [i for i in range(1, N+1)]
answer = []
num = 0

for _ in range(N):
    num += K-1
    if num >= len(N_list):
        num = num % len(N_list)

    answer.append(str(N_list.pop(num)))
print("<", ", ".join(answer)[:], ">", sep='')