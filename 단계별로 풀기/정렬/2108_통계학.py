test_case = int(input())
n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

print(round(sum(num_list)/n))

num_list.sort()
print(num_list[int((n-1)/2)])

cnt = dict()
for i in range(1, n+1):
    cnt[i] = []

max_count = 1
count = 1
