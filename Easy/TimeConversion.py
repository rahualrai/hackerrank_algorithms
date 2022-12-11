def timeConversion(s):
    # Write your code here
    period = s[-2:]
    time = s[:-2]
    hour = int(time[:2])
    
    if period == 'PM' and hour < 12:                
        time = str(hour + 12) + time[2:]

    if period == 'AM' and hour == 12:
        time = '00' + time[2:]
        
    return time