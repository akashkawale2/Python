#reverse list
def reverse_l(li):
    length = len(li)
    for i in range(length//2):
        li[i],li[length-i-1] = li[length-i-1],li[i]

def reverse_l_2
li = [1,2,3,4,5,6]
reverse_l(li)
print(li)