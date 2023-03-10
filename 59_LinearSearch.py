#Linear Search

        # n = int(input())

        # li = [int(x) for x in input().split()]

        # ele = int(input())
        # isFound = False

        # for i in range(len(li)):
        #     if ele == li[i]:
        #         print(i)
        #         isFound = True
        #         break
        # if isFound == False:
        #     print(-1)    
    
#linear search through functions
def linearSearch(li, ele):
    for i in range(len(li)):
        if li[i] == ele:
            return i
    return -1



li = [2,3,4,5,62,3,6,3,1,6]
index = linearSearch(li,22)
print(index)

