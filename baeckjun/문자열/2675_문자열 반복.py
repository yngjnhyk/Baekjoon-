test_case = int(input())
for _ in range(test_case):
    R, S = input().split()
    for i in S:  #ex)S = hello, hello라는 문자열을 i에 넣어 반복해라.
        print(i * int(R), end="")  #for문을 통해 문자열을 반복하면 각 문자를 분리해 ('h', 'e', 'l', 'l', 'o') 반복한다. 그러므로, i를 처음 문자열로 받은 R을 int를 통해 정수로 바꿔 R만큼 반복해 출력한다.
    print()  #줄넘김
