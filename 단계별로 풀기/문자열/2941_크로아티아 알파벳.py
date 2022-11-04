croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i, '*')  #replace를 통해 주어진 단어 word에서 크로아티아 알파벳인 i를 기호 '*'로 변환시키고, 그 값이 word라는 변수에 다시 적용된다.
print(len(word))

#이 문제는 단어가 주어졌을때, 실제로 해당 단어를 크로아티아 알파벳으로 변환시켜주지 않고, 출력해야 하는 건 크로아티아의 갯수라는 점이다.