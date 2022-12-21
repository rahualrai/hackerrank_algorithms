def largestPermutation(k, arr):
    # Write your code here
    n = len(arr)
    max_index_dict = {}
    for i in range(n):
        max_index_dict[arr[i]] = i
    for i in range(n):
        if k == 0:
            break
        if arr[i] == n - i:
            continue
        else:
            max_elem = n - i
            max_index = max_index_dict[max_elem]
            arr[i], arr[max_index] = arr[max_index], arr[i]
            max_index_dict[arr[i]] = i
            max_index_dict[arr[max_index]] = max_index
            k -= 1
    return arr