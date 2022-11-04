A, B = map(int, input().split())
fake_A = int(str(A)[::-1])
fake_B = int(str(B)[::-1])
fake_list = [fake_A, fake_B]
print(max(fake_list))