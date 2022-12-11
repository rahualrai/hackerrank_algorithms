def getMoneySpent(keyboards, drives, b):
    max_cost = 0
    
    for keyboard in keyboards:
        for drive in drives:
            
            total = keyboard + drive
            
            if total > max_cost and total <= b:
                max_cost = total
        
    if max_cost == 0:
        return -1
    
    else:
        return max_cost