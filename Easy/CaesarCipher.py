def caesarCipher(s, k):
    # Write your code here
    cipher = ''
    for char in s:
        if char.isalpha():
            num = ord(char)
            num += k
            
            if char.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif char.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            
            cipher += chr(num)
        else:
            cipher += char
            
    return cipher