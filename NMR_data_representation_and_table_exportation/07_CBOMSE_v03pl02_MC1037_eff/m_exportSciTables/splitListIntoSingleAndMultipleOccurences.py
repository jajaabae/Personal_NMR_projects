def splitListIntoSingleAndMultipleOccurences(aList):
    seen = set()
    multiple = set()
    for x in aList:
        if x not in seen:
            seen.add(x)
        else:
            multiple.add(x)
    singles = list(seen - multiple)
    multiple = list(multiple)
    return singles, multiple
