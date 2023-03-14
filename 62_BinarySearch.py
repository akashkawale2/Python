def BinarySearch(arr, x):
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid -1
        return -1
arr = [1,3,4,5,6,22,26,31,52]
x =3
index = BinarySearch(arr, x)
print(index)