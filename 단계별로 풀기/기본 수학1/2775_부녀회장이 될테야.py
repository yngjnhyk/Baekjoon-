T = int(input())
for _ in range(T):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num)]  #0층의 리스트를 1부터 주어진 num의 값 -1만큼 x를 반복해 만든다. ex)num = 3이면, f0 = [1,2,3]이다.
    for k in range(floor):  #다음 나올 아래 내용을 k로 두고, k를 주어진 floor의 값만큼 반복해라.
        for i in range(1, num):  #i를 1부터 num - 1만큼 반복해라.
            f0[i] += f0[i-1]  #f0의 값은 f0의 값에 f0의 i-1번째 오는 값을 더한 값으로 업데이트된다. ex)floor =2, num = 3이고, 첫번째 for i문을 통해 f0을 반복했으면, f0[1]은 반복되기 전 f0의 1번째 있는 값에서 0번째 값은 반복을 통해 업데이트 됐으니 반복된(업데이트된) 첫번째 반복 f0의 0번째 값을 더한 값이 된다.
    print(f0[-1])  #num만큼 반복했으니 나열된 f0 리스트를 보면 마지막 값이 구하고자 하는 값이 된다.
