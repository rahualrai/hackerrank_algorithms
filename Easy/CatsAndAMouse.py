def catAndMouse(x, y, z):
    cat_a = abs(x-z)
    cat_b = abs(y-z)
    
    if cat_a<cat_b:
        return("Cat A")
    elif cat_a>cat_b:
        return("Cat B")
    else:
        return("Mouse C")