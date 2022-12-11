def breakingRecords(scores):

    highest = scores[0]
    lowest = scores[0]
    record = [0,0]
    
    for i in range(1,len(scores)):
        now = scores[i]
        if now > highest:
            record[0] += 1
            highest = now
        elif now < lowest:
            record[1] += 1
            lowest = now
            
    return record