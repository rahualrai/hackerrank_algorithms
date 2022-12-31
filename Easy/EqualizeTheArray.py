def equalizeArray(arr):
    # Write your code 
    nums = set(arr)
    count = 0
    for num in nums:
        if arr.count(num) > count:
            count = arr.count(num)

    return len(arr) - count