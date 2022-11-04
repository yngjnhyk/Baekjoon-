A, B = [], []  #A, B에 행렬을 넣기 위해 리스트를 만들어둔다.

N, M = map(int, input().split())

for row in range(N):  #N번만큼 row를 반복해라.
    row = list(map(int, input().split()))  #row는 한 칸씩 띄워쓰여진 정수 값들을 넣은 리스트이다.
    A.append(row)  #row를 A리스트에 넣어라.
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
for row in range(N):  #N번만큼 row를 반복해라. 행렬의 가로횡
    for col in range(M):  #M번만큼 col를 반복해라. 행렬의 세로횡
        print(A[row][col] + B[row][col], end=' ')  #end = ' ' 를 통해 띄어쓰기로 열을 구분하여 출력
    print()
