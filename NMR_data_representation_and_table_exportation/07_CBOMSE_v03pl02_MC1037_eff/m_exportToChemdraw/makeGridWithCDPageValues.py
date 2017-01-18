from m.mfi import imp
exec(imp())

def makeGridWithCDPageValues(groups):
    """
    #print groups
    def TMP01():
        print '-'
        for g in groups:
            if not groups[g] == -1:
                print g, groups[g]
    #TMP01()
    #"""


    i('getNumOfGroups')
    nOfGroups = getNumOfGroups(groups)
    #print 'nOfGroups:', nOfGroups

    ### Make grid ###
    i_fsf('m_exportToChemdraw.splitAxis')
    i_fsf('m_exportToChemdraw.makeGridForFragments')

    CDPageX = [4.35, 539.50-20]
    CDPageY = [12.24, 790.50-30]
    CDPageX = [4.35, 539.50*2-200]
    CDPageY = [12.24, 790.50-30]

    #pageX = 500
    #pageY = 800
    pageX = CDPageX
    pageY = CDPageY
    #print 'pageX,y', pageX, pageY
    grid = makeGridForFragments(nOfGroups, pageX, pageY)
    #print grid
    return grid
