# i = 1
# while i < 10:
#     print(i)
#     i = i + 1
# else:
#     print("this is will be printed at the end")

n = input()
for d in range(2, n, 1):
    if n % d == 0:
        break
else:
    print("prime number")