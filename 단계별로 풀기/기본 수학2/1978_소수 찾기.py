n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1:  #for문을 통해 주어진 numbers의 값들을 반복 중인 num의 값이 1보다 크면(=1이상이 소수의 조건이 되기 때문),
        for i in range(2, num):  #200-자료구조1 ~ num-1만큼 i에 대입해 i가 반복해라.
            if num % i == 0:  #numbers의 값들, 즉 num의 값이 (200-자료구조1 ~ num-1)에 의해 나눠질 경우(소수가 아님),
                error += 1  #error라는 변수에 1을 더해라.
        if error == 0:  #num의 값이 위 for i문과 if문을 거치고, error가 0일 경우(num의 값이 소수일 경우),
            sosu += 1  #sosu라는 변수에 1을 더해라.
print(sosu)