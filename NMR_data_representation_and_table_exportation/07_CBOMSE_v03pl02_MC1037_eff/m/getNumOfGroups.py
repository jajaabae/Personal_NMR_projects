def getNumOfGroups(groups):
    max=-1
    for g in groups:
        if groups[g] > max:
            max = groups[g]
    return max
