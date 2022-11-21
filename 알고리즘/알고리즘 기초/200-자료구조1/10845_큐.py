from sys import stdin

N = int(stdin.readline())
Que = []

for i in range(N):
    A = stdin.readline().split()
    order = A[0]

    if order == 'push':
        Que.append(A[1])
    elif order == 'pop':
        if Que:
            print(Que.pop(0))
        else:
            print(-1)
    elif order == 'size':
        print(len(Que))
    elif A[0] == 'empty':
        if len(Que) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[0])
    elif order == 'back':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[-1])
