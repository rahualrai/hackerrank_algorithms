def staircase(n):
    # Write your code here
    blanklist = list(" "*n)
    for i in range(n):
        blanklist.append('#')
        blanklist.pop(0)
        print("".join(blanklist))
