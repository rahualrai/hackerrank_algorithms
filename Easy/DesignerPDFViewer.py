def designerPdfViewer(h, word):
    max_height = 0
    for i in word:
        n = ord(i)-97
        height = h[n]
        max_height = max([max_height,height])
    return max_height*len(word)