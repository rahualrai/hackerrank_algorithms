def insertionSort1(n, arr):
    # Write your code here
    key = arr[n-1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        for a in arr:
            print(a, end=" ")
        print()
        j -= 1
    arr[j+1] = key
    for a in arr:
        print(a, end=" ")

# time complexity = O(n^2) 