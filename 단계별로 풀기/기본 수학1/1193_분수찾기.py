x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    top = x - num_count
    under = num - i + 1
else:
    top = num - (x - num_count) + 1
    under = x - num_count

print(f"{top}/{under}")