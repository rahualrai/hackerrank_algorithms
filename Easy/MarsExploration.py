def marsExploration(s):
    # Write your code here
    count = 0
    for i in range(len(s)):
        if s[i] != 'SOS'[i % 3]:
            count += 1
    return count