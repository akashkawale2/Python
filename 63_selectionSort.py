def selectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        min_index = i
        for j in range(i+1,length):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i],arr[min_index] = arr[min_index], arr[i]
    
    
arr = [6,1,9,22,87,4,99,5,6,2,55,33,7,3,]
selectionSort(arr)
print(arr)
