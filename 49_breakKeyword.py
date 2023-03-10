# i = 1
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i = i+1
    
    
n = input()
d = 2
flag = False
while(d<n):
    if (n%d == 0):
        flag = True
        break
    d =d+1

if flag:
    print("not prime")
else:
    print("prime")