N = int(input())
group_word = 0
for _ in range(N):
    word = input()
    error = 0  #그룹단어가 아니라면, error에 값이 들어가기 위해 변수 error = 0을 둔다.
    for index in range(len(word)-1):  #바로 다음 내용에 index를 통한 위치값을 이용해 지정글자와 지정글자 + 1과 같은지 아닌지 비교해야 하기 때문에 index범위를 0에서 입력받은 값인 word의 글자개수 - 1까지 둔다.
        if word[index] != word[index+1]:  #index=0,1,..word의 글자 개수 - 1까지 이기 때문에 word[0]와 word[1]가 다르면,
            new_word = word[index+1:]  #word[1]부터 word[0]이후에 글자들은 new_word이다. -> word[0,1..] = word[0] + new_word
            if new_word.count(word[index]) > 0:  #new_word에서 word[0]의 개수를 셋을 때, 0보다 크면, -> new_word에서 word[0]가 한 글자라도 있다면,
                error += 1  #error는 error + 1이다.
    if error == 0:  #글자 하나씩 대입해 끝까지 해보았을 때, 지정글자와 지정글자가 같거나, 같지 않더라도 같지 않은 순간의 지정글자가 이후에도 없어서 error = 0이라면,
        group_word += 1  #group_word는 group_word + 1이다.
print(group_word)

#abaa