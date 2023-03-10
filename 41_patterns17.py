#     1
#    232
#   34543
#  4567654
# 567898765
from __future__ import print_function
n = input()
i = 1
while i <= n:
    j = 1
    while j <= n -i:
        print(" ",end="")
        j = j + 1
    j = 1
    k = i
    while j <= i:
        print(k,end="")
        k = k+1
        j = j+1
    j = i-1
    k = k-2
    while j >= 1:
        print(k,end="")
        k=k-1
        j=j-1
    print()
    i=i+1 
           