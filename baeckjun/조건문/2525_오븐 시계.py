hour, min = map(int, input().split())
add = int(input())

hour += add // 60 #hour은 add값에 60을 나눈 정수 값으로 재할당된다.
min += add % 60 #min은 add값을 60으로 나눈 나머지 값, 재할당된다.

if(min >= 60):
    min -= 60
    hour += 1

if(hour >= 24):
    hour -= 24

print(hour,min)