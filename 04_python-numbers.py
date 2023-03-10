a1 = 23
a2 = 3.4
a3 = 4 + 5j #complex
print(a1)
print(a2)
print(a3)
print(type(a1))
print(type(a2))
print(type(a3))

a = 10
print(id(a))
a = a + 1
print(id(a))

a = 256
b = 256
print(id(a)) #same address 
print(id(b)) #SAME ADDRESS

#PYTHON DOING THIS OPTIMISATION ONLY IN RANGE OF -5 TO 256 BECOUSE IT IS VERY COMMON IN  USE