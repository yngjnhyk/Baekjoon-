import sys

test_case = int(sys.stdin.readline())
arr_list = []

for i in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    arr_list.append([b, a])

arr_list.sort()

for i in range(test_case):
    print(arr_list[i][1], arr_list[i][0])
