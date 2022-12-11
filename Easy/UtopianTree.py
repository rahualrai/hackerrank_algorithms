def utopianTree(n):
    height = 1
    while t<n:
        if t%2==0:
            height*=2
        else:
            height+=1
        t+=1
    return height