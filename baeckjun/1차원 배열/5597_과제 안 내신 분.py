attendance = [i for i in range(1, 31)]
for _ in range(28):
    attendance.remove(int(input()))  #입력된 값을 attendance 리스트에서 삭제해라.

print(min(attendance), max(attendance))