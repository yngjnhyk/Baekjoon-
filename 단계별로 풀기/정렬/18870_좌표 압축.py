import sys
test_case = int(input())

number_list = list(map(int, sys.stdin.readline().rstrip().split()))

set_Number = set(number_list)
set_Number_list = list(set_Number)
set_Number_list.sort()

num_dict = {}
for i in range(len(set_Number_list)):
    num_dict[set_Number_list[i]] = i

print(num_dict)