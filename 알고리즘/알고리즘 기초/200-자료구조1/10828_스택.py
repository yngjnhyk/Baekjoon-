import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    word = input().split()
    order = word[0]
    if order == 'push':
        stack.append(int(word[1]))
    elif order == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif order == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
