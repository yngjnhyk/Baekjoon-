test_case = int(input())
words_list = []
for _ in range(test_case):
    word = input()
    words_list.append(word)

word_list = list(set(words_list))
word_Len_list = []

for i in word_list:
    word_Len_list.append((len(i), i))

result = sorted(word_Len_list)  #[(1, 'i'), (2, 'im'), (2, 'it'), (2, 'no'), (3, 'but'), (4, 'more'),

for len_words, words in result:
    print(words)