start_num, last_num = map(int, input().split())

for num in range(start_num, last_num+1):
    if num == 1:
        continue  #소수는 1보다 높은 숫자이므로 start_num ~ last_num 범위에 1이 있다면 continue를 통해 아래 코드를 실행하지 않고 건너뛴다.
    for i in range(2, int(num ** 0.5)+1):  #start_num~last_num 사이에서 반복 중인 num의 값이 소수인지 확인하는 방법은
        if num % i == 0:  #num의 제곱근값이나 작은 수까지 num을 나눠보고 나누어 떨어지면은 소수가 아니다.
            break  #그러므로 해당 제곱근 이상의 숫자에 대해 더 이상 검사할 필요가 없으므로 for i문을 멈춘다.
    else:
        print(i)  #그렇지 않고, 나눠지지 않는다면, i를 출력한다.
