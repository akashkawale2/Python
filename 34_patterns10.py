# ABCD
# BCDE
# CDEF
# DEFG

from __future__ import print_function

n = input()
i = 1
while i <= n:
    j =1
    start_char = chr(ord('A')+i-1)
    while j <= n:
        charP = chr(ord(start_char)+j-1)
        print(charP, end='')
        j = j+ 1
    print()
    i = i +1