x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('200-자료구조1')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
else:
    pass