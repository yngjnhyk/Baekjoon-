test_case = int(input())
numbers = list(map(int, input().split()))
sum_list = [numbers[0]]

for i in range(len(numbers) - 1):
    sum_list.append(max(sum_list[i] + numbers[i + 1], numbers[i +1]))
print(max(sum_list))