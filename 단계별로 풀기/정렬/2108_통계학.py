import sys
from collections import Counter

test_case = int(sys.stdin.readline())
num_list = []

for _ in range(test_case):
    num_list.append(int(sys.stdin.readline()))

print(round(sum(num_list)/test_case))

print(sorted(num_list)[len(num_list)//2])


count = Counter(num_list)
order = count.most_common()
max_frequency = order[0][1]

frequency_list = []
for i in order:
    if i[1] == max_frequency:
        frequency_list.append(i[0])

if len(frequency_list) == 1:
    print(frequency_list[0])
else:
    print(sorted(frequency_list)[1])

print(max(num_list) - min(num_list))


