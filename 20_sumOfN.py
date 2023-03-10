# Given an integer n, find and print the sum of numbers from 1 to n.

n = input()
i = 1
s = 0
while i <= n:
    s = s + i
    i  = i + 1
    
print(s)