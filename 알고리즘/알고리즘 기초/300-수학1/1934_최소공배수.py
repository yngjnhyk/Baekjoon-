import sys

test_case = int(input())
A, B = map(int, sys.stdin.readline().split())
a, b = A, B

cnt = 0

while cnt < test_case:
    a = a % b
    a, b = b, a
    cnt += 1

print(A * B // a)  # lcm
