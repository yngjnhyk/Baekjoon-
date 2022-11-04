test_case = int(input())

for _ in range(test_case):
    oxs = input()
    score = 0
    sum_score = 0
    for o in oxs:
        if o == 'O':
            score += 1
        else:
            score = 0
        sum_score += score  #sum_score는 sum_score + score이다.
    print(sum_score)