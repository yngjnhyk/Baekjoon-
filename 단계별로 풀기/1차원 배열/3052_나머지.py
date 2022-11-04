nums = set()  #nums는 집합{}(키가 없는 딕셔너리)이다.
for _ in range(10):
    i = int(input())
    nums.add(i % 42)  #반복되고 있는 i값을 42로 나눈 나머지 값을 nums라는 집합에 넣어라.
print((len(nums)))  #nums의 갯수를 프린트해라.