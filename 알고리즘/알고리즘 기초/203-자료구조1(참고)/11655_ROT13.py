word = list(input())
answer = ""

for i in word:
    if i.isupper():
        i = ord(i) + 13
        if i > 90:
            i -= 26
        answer += chr(i)
    elif i.islower():
        i = ord(i) + 13
        if i > 122:
            i -= 26
        answer += chr(i)
    else:
        answer += i
print(answer)