test_case = int(input())

for _ in range(test_case):
    sentence = list(input().split())
    reversed_sentence = []
    for word in sentence:
        reversed_word = word[::-1]
        reversed_sentence.append(reversed_word)
    answer = " ".join(reversed_sentence)
    print(answer)
