word = input()
alphabet = list(range(97, 123))  #alphabet은 아스키코드 숫자범위를 이용해 [a, b, c, d,...y, z]이다.

for i in alphabet:
    print(word.find(chr(i)))  #find를 이용해 a,b,c,..들이 어디에 위치하고 있는지 a,b,c,..대신 위치값을 표현하게 된다.
