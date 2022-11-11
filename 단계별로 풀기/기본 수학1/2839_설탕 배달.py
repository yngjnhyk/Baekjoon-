N = int(input())

bag_cnt = 0
while N >= 0:  #주어진 설탕의 무게 N값이 0이 될 때까지 -3kg씩 해서 5의 배수까지 맞추고, -3kg을 한 번 할 때마다 봉지개수 bag_cnt에 1씩 더하는 반복을 할 것이다.
    if N % 5 == 0:  #주어진 설탕의 무게가 5의 배수일 경우,
        bag_cnt += (N // 5)  #봉지의 개수는 설탕의 총무게 N값을 5로 나눈 몫이다.
        print(bag_cnt)
        break
    N -= 3
    bag_cnt += 1
else:
    print(-1)