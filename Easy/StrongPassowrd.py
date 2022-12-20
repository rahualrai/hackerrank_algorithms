def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"
    
    missing = 0
    if not any(char.isdigit() for char in password):
        missing += 1
    if not any(char.islower() for char in password):
        missing += 1
    if not any(char.isupper() for char in password):
        missing += 1
    if not any(char in special_characters for char in password):
        missing += 1
    if n + missing < 6:
        missing += 6 - (n + missing)
    return missing