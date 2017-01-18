def splitAxis(sqrt, pageTouple):
    #print pageTouple
    page = pageTouple[1] - pageTouple[0]
    pageMargin = pageTouple[0]
    borderMargin=10./100*page
    #margin=5./100*page
    width = float(page) #-2*borderMargin)
    sectionWidth = width/sqrt
    #print 'sw', sectionWidth
    sectionMargin = sectionWidth*5./100
    sectionPrintLength = sectionWidth - sectionMargin*2
    #print 'sw', sectionWidth
    #split=[margin]
    split=[[0]]
    for i in range(1, (int(sqrt)+1)):
        #print i
        #start = split[-1][-1]+sectionMargin*2
        #end = start+sectionPrintLength
        start = split[-1][-1]+sectionMargin*2
        end = start+sectionPrintLength
        split.append([start, end])
    split = split[1:len(split)]
    #print split
    return split