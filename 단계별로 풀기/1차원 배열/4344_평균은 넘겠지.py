test_case = int(input())
for _ in range(test_case):
    scores = list(map(int, input().split()))
    score_average = sum(scores[1:])/scores[0]  #score_average는 score리스트의 1번째(0번째 아님)부터 나머지까지의 합을 0번째로 나눈 값이다.
    count = 0  #평균을 넘은 학생 수
    for score in scores[1:]:  #score를 scores 1번째부터 나머지 부분에서 반복해라.
        if score > score_average:
            count += 1
    rate = count/scores[0] * 100  #rate는 count를 scores의 0번째로 나눈 몫을 곱하기 100해라.
    print(f'{rate:.3f}%')  #rate를 소수 3째자리까지하고 뒤에 %를 붙여서 프린트해라