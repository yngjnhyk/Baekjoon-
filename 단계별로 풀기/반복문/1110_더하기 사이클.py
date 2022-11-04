input_num = int(input())

num = input_num  #num 변수에 input_num을 지정
cnt = 0  #사이클 카운트
while True:
    sum_num = (num // 10) + (num % 10)  #sum_num은 num의 10의 자릿수와 num의 1의 자릿수를 더한 값이다.
    new_num = ((num % 10) * 10) + (sum_num % 10)  #new_num은 num의 10의 자릿수엔 1의 자릿수를 두고, 1의 자릿수엔 sum_num의 1의 자릿수를 둔 값이다.
    cnt += 1  #사이클 카운트 횟수 세기
    if new_num == input_num :  #new_num이 input_num의 값과 같다면
        break
    num = new_num  #while문이 break되지 않으면, num 변수에 새로 생성한 수 new_num을 지정하고, while문을 처음부터 반복한다.
print(cnt)