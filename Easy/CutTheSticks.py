def cutTheSticks(arr):
    result = []
    while arr:
        result.append(len(arr))
        cut_length = min(arr)
        arr = [x - cut_length for x in arr if x - cut_length > 0]
    return result