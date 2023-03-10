n = input()
flag = False
for d in range(2,n,1):
    if n%d == 0:
        Flag = True

if flag:
    print("Not prime")
else:
    print("prime")