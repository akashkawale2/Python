# Given a number N, print sum of all even numbers from 1 to N.

n = input()

i = 1 
s = 0
while i <= n:
    if i % 2 == 0:
        s = s + i 
    i = i + 1
    
print(s)