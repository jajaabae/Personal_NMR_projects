def bondsClean(bonds):
    newBonds=[]
    for b in bonds:
        if b not in newBonds:
            newBonds.append(b)
    return newBonds
