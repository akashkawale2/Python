#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

from __future__ import print_function

n = input()
i = 1
n1 = (n+1)/2
n2 = n1-1
#first half
while i <= n1:
    j = 1
    while j <= n1-i:
        print(" ",end="")
        j=j+1
    j = 1
    while j <= 2*i-1:
        print("*",end="")
        j=j+1
    print()
    i=i+1    
    
# second Half
i = n2
while i >= 1:
    j = 1
    while j <= n2-i+1:
        print(" ",end="")
        j = j+1
    j =1
    while j <= 2*i-1:
        print("*",end="")
        j=j+1
    print() 
    i = i-1   