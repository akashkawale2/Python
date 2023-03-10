#     1
#    121
#   12321
#  1234321
# 123454321
from __future__ import print_function
n = input()
i=1
while i <= n:
    spaces = 1
    while spaces <= n-i:
        print(" ",end="")
        spaces = spaces + 1
    j = 1
    while j <= i:
        print(j, end="")
        j = j+1
    j = i -1
    while j >= 1:
        print(j, end="")
        j = j-1
    print()
    i = i +1