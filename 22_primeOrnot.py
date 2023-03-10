n = input()

d = 2 
flag = False
while d < n:
    if n % d == 0:
        flag = True
    d = d+1 

if flag:
    print("N is Not prime")
else:
    print("N is Prime")