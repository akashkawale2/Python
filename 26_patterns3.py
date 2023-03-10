#1111
#2222
#3333
#4444

from __future__ import print_function

n = input()
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i, end='')
        j = j+1
    print()
    i=i+1    