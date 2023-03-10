# 1
# 23
# 345
# 5678

from __future__ import print_function

n = input()
i = 1 
while i <= n:
    j = 1
    p = i
    while j <= i:
        print(p, end='')
        p= p+1
        j = j + 1
    print()
    i = i + 1