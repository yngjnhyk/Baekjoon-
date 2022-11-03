numbers = list(range(1, 10_001))  #1부터 10,000까지 들어있는 리스트를 만든다.
remove_list = []  #이후에 만들어 둔 생성자 숫자들 list = 삭제할 숫자 list
for num in numbers :  #ex) num=850
    for n in str(num):  #ex) n = str(num) = "8", "5", "0"
        num += int(n)  #ex) 850 = 850 + 8 + 5
    if num <= 10000:  #10,000보다 작거나 같은 생성자를 제외한 셀프 넘버를 출력해야 하기 때문에 생성자 또한 10,000보다 작거나 같은 조건문을 붙인다.
        remove_list.append(num)  #생성자 숫자들 list에 생성자들을 넣는다.

for remove_num in set(remove_list):  #set을 통해 생성자 숫자들 중에 중복되는 숫자들을 제거한 뒤 remove_num이라는 변수에 넣어 반복한다.
    numbers.remove(remove_num)  #1부터 10,000까지 있는 숫자들 중 생성자 숫자들을 제거해 numbers 리스트에 셀프 넘버들만을 남겨둔다.
for self_num in numbers:  #셀프 넘버만을 남겨둔 numbers리스트를 self_num이라는 변수에 대입해 반복해라.
    print(self_num)