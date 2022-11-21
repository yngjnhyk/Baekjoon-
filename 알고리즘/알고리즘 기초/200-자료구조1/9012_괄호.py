test_case = int(input())

for _ in range(test_case):
    bracket = input()
    bracket_list = list(bracket)
    cnt = 0
    for i in bracket:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')



