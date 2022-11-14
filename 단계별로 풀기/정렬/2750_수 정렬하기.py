test_case = int(input())

num_list = []  #입력된 값들을 담을 비어있는 리스트

for _ in range(test_case):
    num = int(input())
    num_list.append(num)  #입력된 값들을 미리 만들어둔 num_list에 넣는다.

num_list.sort()  #num_list에 있는 값들을 리스트 내에서 오름차순으로 정렬한다.

for i in num_list:  #하나씩 반복해 출력
    print(i)
