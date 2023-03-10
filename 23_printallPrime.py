# print numbers which is prime till n 

n = input()
k = 2
while k <= n:
    d = 2 
    flag = False
    while d < k:
        if k % d == 0:
            flag = True
        d = d+1 
    if not(flag):
        print(k)
    k = k+1

