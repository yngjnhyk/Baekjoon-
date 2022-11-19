words = input().upper()  #입려된 값을 모두 대문자로 바꾼다.
alphabet = list(set(words))  #입력된 값 words에서 기존 단어의 순서는 지켜지지 않지만, set을 이용해 중복된 값을 제거한 후 문자열 하나씩 alphabet 리스트에 넣는다.

cnt_list = []
for i in alphabet:  #ex)words = hello, alphabet = ['O', 'E', 'L', 'H']이면, 하나씩 i에 대입해 반복해라.
    cnt = words.count(i)  #처음에 주어진 값 HELLO에서 각 문자열이 몇개인지 센다. ['O', 'E', 'L', 'H'] -> 1,200-자료구조1,1,1가 cnt이다.
    cnt_list.append(cnt)  #cnt를 cnt_list에 넣어 list형태로 바꾼다.

if cnt_list.count(max(cnt_list)) > 1:  #cnt_list에서 최댓값의 갯수가 1보다 크면(=최댓값이 둘 이상이면)
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))  #cnt_list의 최댓값의 위치를 cnt_list에서 어디에 위치하고 있는지 그 위치값이 max_index이다.
    print(alphabet[max_index])  #alphabet리스트(['O', 'E', 'L', 'H'])에서 cnt_list의 최댓값의 위치값만큼의 위치에 있는 문자열을 출력해라.