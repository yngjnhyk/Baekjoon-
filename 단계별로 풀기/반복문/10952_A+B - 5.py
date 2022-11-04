while True:  #n값이 정해져있지 않기 때문에 while:True를 통해 계속 반복하게 됨.
    a, b = map(int,input().split())
    if(a == 0 and b ==0):
        break
    else:
        print(a+b)