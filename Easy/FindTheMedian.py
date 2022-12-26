def findMedian(arr):
    # Write your code here
    arr.sort()
    length = len(arr)
    if length % 2 == 0:
        median = (arr[length // 2] + arr[length // 2 - 1])/2
    else:
        median = arr[length // 2]
    return median