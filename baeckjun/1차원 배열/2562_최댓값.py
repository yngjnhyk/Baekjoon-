numbers = []
for _ in range(9):  #아래 내용을 아홉번 반복해라.
    i = int(input())  #i를 변수로 값을 입력한다.
    numbers.append(i)  #입력값을 numbers리스트 안에 넣어라.

print(max(numbers))
print(numbers.index(max(numbers)) + 1)  #numbers리스트 안에 있는 값 중 가장 큰 값의 위치에서 1을 더하고 이를 프린트해라.