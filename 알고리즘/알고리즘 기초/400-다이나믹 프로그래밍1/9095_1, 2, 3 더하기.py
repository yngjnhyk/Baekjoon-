test_case = int(input())
s = [1, 2, 4]
for i in range(3, 10):
    s.append((s[i - 3] + s[i - 2] + s[i - 1]))
for i in range(test_case):
    n = int(input())
    print(s[n-1])