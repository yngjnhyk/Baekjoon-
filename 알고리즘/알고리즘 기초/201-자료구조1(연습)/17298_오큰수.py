N = int(input())
numbers = list(map(int, input().split()))

stack = [0]
answer = [-1] * N

for i in range(1, N):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)
