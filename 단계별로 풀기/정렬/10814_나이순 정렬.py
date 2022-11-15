test_case = int(input())
member_list = []


for _ in range(test_case):
    age, name = input().split()
    member_list.append([int(age), name])

member_list.sort(key=lambda x: x[0])

for i in range(test_case):
    print(member_list[i][0], member_list[i][1])
