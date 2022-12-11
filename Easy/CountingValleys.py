def countingValleys(steps, path):
    altitude = 0
    valley = 0
    # whether the hiker is currently in a valley
    in_valley = False
    
    for char in path:
        
        if char == "U":
            altitude+=1
            
            # if hiker was in valley and just exited
            if in_valley and altitude>=0:
                in_valley = False
                
        elif char == "D":
            altitude-=1
            
            # if hiker wasn't in valley and just entered
            if not in_valley and altitude<0:
                valley+=1
                in_valley = True

    return valley
            