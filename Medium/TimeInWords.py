def timeInWords(h, m):
    # Write your code here
    numbers = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    21:"twenty one",
    22:"twenty two",
    23:"twenty three",
    24:"twenty four",
    25:"twenty five",
    26:"twenty six",
    27:"twenty seven",
    28:"twenty eight",
    29:"twenty nine"
    }
    if m == 0:
        return numbers[h] + " o' clock"
    elif m == 15:
        return "quarter past " + numbers[h]
    elif m == 30:
        return "half past " + numbers[h]
    elif m == 45:
        return "quarter to " + numbers[h+1]
    elif m == 1:
        return numbers[m] + " minute past " + numbers[h]
    elif m == 59:
        return numbers[60-m] + " minute to " + numbers[h+1]
    elif m < 30:
        return numbers[m] + " minutes past " + numbers[h]
    else:
        return numbers[60-m] + " minutes to " + numbers[h+1]
# time complexity is: O(1)