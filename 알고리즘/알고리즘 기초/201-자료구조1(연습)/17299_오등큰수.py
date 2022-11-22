from collections import Counter
from sys import stdin

N = int(input())
numbers = list(map(int, stdin.readline().split()))
numbers_count = Counter(numbers)
stack = [0]
answer = [-1] * N

for i in range(1, N):
    while stack and numbers_count[numbers[stack[-1]]] < numbers_count[numbers[i]]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)
