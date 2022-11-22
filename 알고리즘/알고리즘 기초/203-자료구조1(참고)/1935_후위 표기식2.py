test_case = int(input())
expression = input()
num_list = [0] * test_case


for i in range(test_case):
    num_list[i] = int(input())

stack = []

for i in expression:
    if i.isalpha():
        stack.append(num_list[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if i == "+":
            stack.append(str1 + str2)
        elif i == "-":
            stack.append(str1 - str2)
        elif i == "*":
            stack.append(str1 * str2)
        elif i == "/":
            stack.append(str1 / str2)
            
print('%.2f' % stack[0])
