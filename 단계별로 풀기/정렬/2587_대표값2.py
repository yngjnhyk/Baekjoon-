num_list = []

for _ in range(5):
    num = int(input())
    num_list.append(num)

num_list.sort()

average = sum(num_list) // len(num_list)

print(average, num_list[2])
