from sys import stdin

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, stdin.readline().split())
answer = ''

while N != 0:
    answer += str(tmp[N % B])
    N //= B

print(answer[::-1])

