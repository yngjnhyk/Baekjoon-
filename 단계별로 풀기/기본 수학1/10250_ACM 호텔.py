test_case = int(input())
for _ in range(test_case):
    H, M, N = map(int, input().split())
    num = N // H + 1  #방 호수는 주어진 순번 N값을 층수H로 나눈 값인 몫에 1을 더한 값이다.
    floor = N % H  #층 수는 주어진 순번 N값을 층수H로 나눈 나머지 값의 정수부분만큼이다.
    if N % H == 0:  #H가 N의 배수일 경우 나머지 값(=floor)이 0이 되므로
        num = N // H  #방 호수는 주어진 순번 N값을 층수H로 나눈 값인 몫이고,
        floor = H  #층 수는 H값의 배수 즉, 꼭대기 층으로 H값이다.
    print(f'{floor * 100 + num}')

