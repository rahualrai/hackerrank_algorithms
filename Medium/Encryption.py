def encryption(s):
    # Write your code here
    length = len(s)
    sqrt = length**0.5
    
    
    # row = int(sqrt) <---- this is unnecessary
    if int(sqrt)==sqrt:
        column = int(sqrt)
    else:
        column = int(sqrt)+1
    
    encrypted_str = [""] * column
    index = 0
    
    for char in s: 
        encrypted_str[index] += char 
        index += 1
        
        if index == column: 
            index = 0
    
    return " ".join(encrypted_str)

# time complexity: O(n)