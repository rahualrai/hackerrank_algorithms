def dayOfProgrammer(year):

    # If the year is a leap year in the Julian calendar, the Day of the Programmer is September 12
    if year < 1918:
        if year % 4 == 0:
            return '12.09.{}'.format(year)
        else:
            return '13.09.{}'.format(year)
        
    # If the year is the transition year of 1918, the Day of the Programmer is September 26 1918
    elif year == 1918:
        return '26.09.1918'         
    
    # If the year is a leap year in the Gregorian calendar, the Day of the Programmer is September 12
    elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return '12.09.{}'.format(year)
    
    # Otherwise, the Day of the Programmer is September 13
    else:
        return '13.09.{}'.format(year)