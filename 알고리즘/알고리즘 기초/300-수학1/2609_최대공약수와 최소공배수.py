import sys

test_case = int(input())

for i in range(test_case):
    A, B = map(int, sys.stdin.readline().strip().split())
    a, b = A, B
    while b != 0:
        a = a % b
        a, b = b, a
    print(A * B // a)  # lcm



