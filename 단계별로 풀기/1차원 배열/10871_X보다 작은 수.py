n,x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] < x :
        print(a[i], end=" ")  #print의 end 기본값이 '\n'으로 설정되어 자동으로 줄바꿈이 되는 것이므로 그 설정을 공백으로 변경해주면 해결할 수 있다.