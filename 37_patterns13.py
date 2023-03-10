# 1111
# 222
# 33
# 4
from __future__ import print_function
n = input()

i = 1
while i <= n:
    j = 1
    while j <= n-i+1:
        print(i,end="")
        j=j+1
    print()
    i=i+1