N = int(input())
result = 0

for i in range(1, N + 1):  #0은 정수가 아니므로, 1 ~ 주어진 값, N까지 i에 대입해 반복한다.
    a = list(map(int, str(i)))
    s = i + sum(a)
    if (s == N):
        result = i
        break

print(result)
