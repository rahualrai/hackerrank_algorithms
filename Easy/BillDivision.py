def bonAppetit(bill, k, b):

    total_bill = sum(bill)
    anna_share = (total_bill - bill[k]) / 2

    if anna_share == b:
        print('Bon Appetit')
    else:
        print(int(b - anna_share))