import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    if not s:
        break
    lower, upper, digit, blank = 0, 0, 0, 0
    for i in range(len(s)):
        if s[i].islower():
            lower += 1
        elif s[i].isupper():
            upper += 1
        elif s[i].isdigit():
            digit += 1
        else:
            blank += 1
    print(lower, upper, digit, blank)
