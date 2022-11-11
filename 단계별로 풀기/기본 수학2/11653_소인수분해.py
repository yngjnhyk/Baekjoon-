N = int(input())

while N != 1:  #주어진 값 N이 1일때까지 반복해라.(N을 나눌 수 있는 가장 작은 소수 i값을 한번씩 출력한다.)
    i = 2  #i는 가장 작은 소수를 표현한 값이다.
    while True:
        if N % i == 0:  #N을 가장 작은 소수 i값으로 나뉠 경우,
            N = N // i  #N값은 N을 i로 나눈 몫이 된다.
            print(i)
            break  #N값이 더 이상 2로 나눠지지 않는 경우, while TRUE문을 중단하고,
        else:
            i += 1  #i에 1을 더해 다시 while TRUE문을 실행한다.

