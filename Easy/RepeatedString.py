def repeatedString(s, n):
    # Write your code here
    a_count = 0
    for letter in s:
        if letter == 'a':
            a_count += 1
            
    string_length = len(s)
    repeat = n // string_length
    a_count *= repeat
    
    remainder = n % string_length
    for i in range(remainder):
        if s[i] == 'a':
            a_count += 1
            
    return a_count