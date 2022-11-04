def hansu(num):  #hansu라는 이름으로 다음 내용을 함수로 만들자.
    hansu_cnt = 0
    for i in range(1, num+1):  #1에서 num으로 넣은 입력값만큼 i에 대입해 반복해라.
        num_list = list(map(int, str(i)))  #ex)i=110, num_list = ['1', '1', '0']이다.
        if i < 100:  #i가 100미만이면 모두 한수이다.(실제로 그러해서 굳이 1~99까지 한수인지 아닌지 알아낼 필요가 없다.)
            hansu_cnt += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:  #ex)i=110, num_list = ['1', '1', '0']이므로 1-1 = 1-0
            hansu_cnt += 1  #성립된다면 hansu_cnt = hansu_cnt + 1
    return hansu_cnt  #성립되지 않는다면 hansu_cnt = hansu_cnt

num = int(input())
print(hansu(num))

