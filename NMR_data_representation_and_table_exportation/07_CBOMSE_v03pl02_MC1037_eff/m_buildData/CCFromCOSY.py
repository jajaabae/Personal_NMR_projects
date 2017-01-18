def CCFromCOSY(correlations, Bonds, Carbons, prelimBonds):
    for cor in correlations:
        if cor[2] == 'c':
            ca=None
            cb=None
            #print cor
            for b1 in Bonds:
                if cor[0] == b1[0] and b1[1] in Carbons:
                    #for c in Carbons: #finds only 1 carbon for an H.
                     #   if b[2]==c:
                            ca=b1[1]
                            #print ca
            for b2 in Bonds:
                    if cor[1] == b2[0] and b2[1] in Carbons:
                        cb=b2[1]
            if ca and cb:
                #print 'ca, cb'
                #print ca, cb
                prelimBonds.append(sorted([ca, cb]))
