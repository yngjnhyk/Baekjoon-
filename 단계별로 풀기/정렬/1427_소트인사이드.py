N = int(input())
N_list = []

for i in str(N):  
    N_list.append(int(i))

N_list.sort(reverse=True)

for x in N_list:
    print(x, end='')
