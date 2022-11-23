S = input()
alphabet_list = [0] * 26


for i in S:
    alphabet_list[ord(i) - ord('a')] += 1

print(*alphabet_list)