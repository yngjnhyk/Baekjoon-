test_case = int(input())
for x in range(1, test_case+1):
    A, B = map(int, input().split())
    print(f'Case #{x}: {A+B}')
