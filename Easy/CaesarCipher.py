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

def caesarCipher(s, k):
    cipher = "" 

    for i in range(len(s)): 
  
        # uppercase characters 
        if (ord(s[i]) >= 65 and
            ord(s[i]) <= 90): 
            cipher += chr((ord(s[i]) + k-65) % 26 + 65) 
  
        # lowercase characters 
        elif (ord(s[i]) >= 97 and
              ord(s[i]) <= 122): 
            cipher += chr((ord(s[i]) + k - 97) % 26 + 97) 
  
        # do not encrypt 
        else: 
            cipher += s[i] 

    return cipher