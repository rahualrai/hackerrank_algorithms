def insertionSort2(n, arr):
    
    # start looping from position 1 to n
    for i in range(1, n):
        
        # set the current element as the key
        key = arr[i]
        
        # set the index to the previous element
        j = i-1
        
        # loop backwards while index is greater than or equal to 0 and the
        # element at the current index is greater than the key
        while j>= 0 and arr[j]>key:
            
            # move the element at the current index one position forward
            arr[j+1] = arr[j]
            
            # decrement the index
            j-=1
            
        # insert the key in its correct position
        arr[j+1] = key
        
        # print the current state of the array
        for a in arr:
            print(a, end = " ")
        print()
        
        # print(" ".join(list(map(str, arr)))) ~alternative~