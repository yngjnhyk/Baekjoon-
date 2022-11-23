S = input()
alphabet_list = list(range(97, 123))

for i in alphabet_list:
    print(S.find(chr(i)), end=" ")

