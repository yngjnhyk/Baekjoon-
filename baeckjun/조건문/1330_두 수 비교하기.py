A, B = map(int, input().split())   #A, B는 input으로 받은 문자열을 split을 통해 나눈 뒤, int함수로 문자열을 정수로 바꾼 값이다.
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')
