def countingSort(arr):
    # Write your code here
    
    count_arr = [0] * (max(arr) + 1)
    for num in arr:
        count_arr[num] += 1
        
    sorted_arr = []
    for num, count in enumerate(count_arr):
        if count > 0:
            sorted_arr.extend([num] * count)
    return sorted_arr