import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())  # sys.stdin.readline() = input()

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)