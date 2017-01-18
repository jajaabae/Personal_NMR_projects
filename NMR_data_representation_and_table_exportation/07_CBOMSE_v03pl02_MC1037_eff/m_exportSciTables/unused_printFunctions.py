#"""
def printData(Carbons, Hydrogens, correlations):
    print correlations
    print
    print Carbons
    print
    print Hydrogens
    print 

def printForCarbons(Carbons, Hydrogens, correlations, NewAtomData):
    for c in Carbons:
        print c, NewAtomData[c]
        for h in Hydrogens:
            if hsqcCor(c, h):
                print '\t', h, NewAtomData[h]

def printAllHydrogens(Carbons, Hydrogens, correlations, NewAtomData):
    tmpList = [
        'pink',
        'Red',
        'green',
        'ThPurple',
        'BrPurple',
        'Mdha',
        'Black',
        #'none',
        #'Unknown',
        ]
    for n in tmpList:
        #print n
        for h in Hydrogens:
            #print NewAtomData[h][5]
            if n in NewAtomData[h][5]:
                #print h, NewAtomData[h]
                #print '\t', h, NewAtomData[h][5], NewAtomData[h][2]
                print n, '\t', h, '\t', NewAtomData[h][2].replace('.', ','), '\t', NewAtomData[h][0]
                if 'C' in NewAtomData[h][4] and not "'" in NewAtomData[h][4]:
                    #print '\t', '\t', NewAtomData[h][4], NewAtomData[NewAtomData[h][4]][2]
                    print n, '\t', NewAtomData[h][4], '\t', NewAtomData[NewAtomData[h][4]][2].replace('.', ','), '\t', NewAtomData[NewAtomData[h][4]][0]
            
def printAtomNames(Carbons, Hydrogens, NewAtomData):
    tmpList = [
        'Leu_a',
        'Leu_b',
        'xxx3',
        'Arg4',
        'Adda5',
        'Glu6',
        'Mdha7',
        ]
    for aa in tmpList:
        for h in Hydrogens:
            if aa in NewAtomData[h][4]:
                print NewAtomData[h][4]
    print
    for aa in tmpList:
        for c in Carbons:
            #print NewAtomData[c]
            if aa in NewAtomData[c][5]:
                print NewAtomData[c][5]

#"""
