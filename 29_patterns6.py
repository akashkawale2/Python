# 1
# 12
# 123
# 1234

from __future__ import print_function

n = input()
i = 1 
while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j = j + 1
    print()
    i = i + 1