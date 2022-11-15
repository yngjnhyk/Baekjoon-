test_case = int(input())
arr_list = []

for i in range(test_case):
    a, b = map(int, input().split())
    arr_list.append([a, b])

arr_list.sort()

for i in range(test_case):
    print(arr_list[i][0], arr_list[i][1])
