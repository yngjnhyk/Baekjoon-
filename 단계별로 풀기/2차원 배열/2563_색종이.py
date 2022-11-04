arr = [[0]*100 for _ in range(100)]  #100*100의 모눈종이 도화지를 만들었다.

for _ in range(int(input())):  #첫줄에 입력된 값만큼 아랫 내용을 반복해라.
    m, n = map(int, input().split())  #m, n은 한 칸씩 띄워서 나열된 정수이다.
    for i in range(m, m+10):  #값을 받은 m ~ m+9만큼 i애 대입해 반복해라.
        for j in range(n, n+10):  #값을 받은 n ~ n+9만큼 j에 대입해 반복해라.
            arr[i][j] = 1  #arr[m~m+9][n~n+9]이면서 하나씩 대입해 반복해라.(ex)[3~12][7~16] -> [3][7],[3][8...]/[4][7][4][8...] 이들 하나하나 값이 처음 arr에서 입력된 0에서 1로 바꿔주는 것이다.
area = 0  #넓이
for i in arr:  #입력값이 0에서 1로 바뀐 애들을 포함한 arr을 i에 하나씩 대입해 반복해라.
    area += i.count(1)  #area는 area에 arr값이 하나씩 들어가 있는 i값에서 count를 통해 1의 갯수를 센 값을 더한 값이다.

print(area)
