def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app = 0
    ora = 0
    for apple in apples:
        if (apple-a)<=10 and (apple-a)<=7:
            app+=1
    for orange in oranges:
        if (orange-a)<=10 and (orange-a)<=7:
            ora+=1
    print(app)
    print(ora)