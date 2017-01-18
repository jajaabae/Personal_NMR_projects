from m.mfi import imp
exec(imp())
def makeGridForFragments(nOfGroups, pageX, pageY):
    import math
    i_fsf('m_exportToChemdraw.splitAxis')
    
    #print nOfGroups
    #if nOfGroups == -1:
    #    nOfGroups=1
    sqrt =  math.ceil(math.sqrt(nOfGroups))
    linePartsX = splitAxis(sqrt, pageX)
    linePartsY = splitAxis(sqrt, pageY)
    #print 'linePartsX:', linePartsX
    #print 'linePartsY:', linePartsY
    grid = []
    for x in linePartsX:
        for y in linePartsY:
           grid.append([x,y])
    #print grid
    #print len(grid)
    return grid
