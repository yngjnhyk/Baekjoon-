import sys

input = sys.stdin.readline

n = int(input())
Deque = []

for i in range(n):
    word = input().split()
    order = word[0]
    if order == 'push_front':
        Deque.insert(0, int(word[1]))
    elif order == 'push_back':
        Deque.append(int(word[1]))
    elif order == 'pop_front':
        if len(Deque) > 0:
            print(Deque.pop(0))
        else:
            print(-1)
    elif order == 'pop_back':
        if len(Deque) > 0:
            print(Deque.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(Deque))
    elif order == 'empty':
        if len(Deque) > 0:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if len(Deque) > 0:
            print(Deque[0])
        else:
            print(-1)
    elif order == 'back':
        if len(Deque) > 0:
            print(Deque[-1])
        else:
            print(-1)