import sys


st1 = list(input())
st2 = []
n = int(input())

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'L' and st1:
        st2.append(st1.pop())
    elif order[0] == 'D' and st2:
        st1.append(st2.pop())
    elif order[0] == 'B' and st1:
        st1.pop()
    elif order[0] == 'P':
        st1.append(order[1])

print(''.join(st1 + list(reversed(st2))))
