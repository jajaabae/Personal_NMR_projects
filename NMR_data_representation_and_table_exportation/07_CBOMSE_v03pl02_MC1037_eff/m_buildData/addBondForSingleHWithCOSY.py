def addBondForSingleHWithCOSY(correlations, getOtherFromCor, Bonds):
    
    #global Bonds
#   "Ca. as above: for all connections:
    for bond in correlations:
        if bond[2]=='c':
    #       for Ha and Hb:
            HSQCa = []
            HSQCb = []
            for otherB in correlations:
    #           if have no bond or have one same C:
                #print len(otherB)
                #print otherB
                #print len(otherB)>2
                if bond[0] in otherB and len(otherB)>2:
                    if otherB[2]=='q': # or if I get another way of assigning the H-C-bond
        #               bond = COSYCorrelation
                        HSQCa += [getOtherFromCor(bond[0], otherB)]
                        #print 'a', bond[0], bond, otherB, getOtherFromCor(bond[0], otherB)
                if bond[1] in otherB and len(otherB)>2:
                    if otherB[2]=='q': # or if I get another way of assigning the H-C-bond
        #               bond = COSYCorrelation
                        HSQCb += [getOtherFromCor(bond[1], otherB)]
                        #print 'b', bond[1], bond, otherB, getOtherFromCor(bond[1], otherB)
            #print 'HSQCa and b:', HSQCa, HSQCb
            #if len(hsqca or hsqcb)=0, or one of a in b, or one of b in a:
            MakeBond=False
            if len(HSQCa)==0 or len(HSQCb)==0:
                MakeBond=True
            if False: #bind HH On Same C
                for a in HSQCa:
                    if a in HSQCb:
                        MakeBond=True
                for b in HSQCb:
                    if b in HSQCa:
                        MakeBond=True
            #MakeCOSYBond if true
            #print MakeBond
            if MakeBond:
                Bonds.append(sorted([bond[0], bond[1], 'c']))
                #print 'made'
            #print
