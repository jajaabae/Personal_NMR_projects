def getOtherFromCor(atom, correlation):
    if correlation[0] == correlation[1]:
        print 'error'
        return None
    elif not atom == correlation[0]:
        return correlation[0]
    elif not atom == correlation[1]:
        return correlation[1]
