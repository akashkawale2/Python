# ABCD
# ABCD
# ABCD
# ABCD

from __future__ import print_function

n = input()
i = 1
while i <= n:
    j = 1
    while j <= n:
        charP = chr(ord('A') + j  - 1)
        print(charP, end='')
        j = j+1
    print()
    i = i + 1
