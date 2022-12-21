def hackerrankInString(s):
    # Write your code here
    check = "hackerrank"
    index = 0
    for i in s:
        if i == check[index]:
            index += 1
            if index == len(check):
                return "YES"
    return "NO"