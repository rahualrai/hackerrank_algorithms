def appendAndDelete(s, t, k):
    if (len(s) + len(t) <= k) or (s == t):
        return 'Yes'
    
    else:
        common_length = 0
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                break
            common_length += 1
        
        operations = len(s)+len(t) - (2*common_length)
        if k >= operations:
            if (k - operations) % 2 == 0:
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'

# time complexity: O(n) where n is the shorter string