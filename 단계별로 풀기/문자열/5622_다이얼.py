alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']  #alphabet_lis를 같은 칸에 있는(=돌리는 시간이 같은) 알파벳끼리 하나의 문자열을 만들어 리스트를 작성해 이들의 위치값을 이용해 걸리는 시간을 구할 예정이다.
word = input()
time = 0

for unit in alphabet_list:  #alphabet_list에 있는 문자열들을 unit에 대입해 반복해라.
    for i in unit:  #alphabet_list를 통해 받은 문자열 'ABC', 'DEF', 'GHI',..들을 'A', 'B', 'C'형태로 나눠 i에 대입해 반복해라.
        for x in word:  #word값을 x에 대입해 반복해라.
            if i == x:  #i와 x가 같다면
                time += alphabet_list.index(unit) + 3  #alphabet_list에 있을 unit('ABC', 'DEF', 'GHI',..)의 위치값에 + 3한 값이 걸리는 시간이다.


print(time)
