def pangrams(s):
    # Write your code here
    abcs = "abcdefghijklmnopqrstuvxyz"
    n = all([char in s.lower() for char in abcs])
    if n:
        return "pangram"
    return "not pangram"
