"""
- ikke kvadrat
- ppm
- lag diagonal
- hent correlations fra a til b og b til a. (for den er ryddet).


#Other:
- add to CD:
    - user-atom-names
    - comments
#"""

def addZeroToHNameAndCNameUnderTen(atom):
    if len(atom)<3 and len(atom)>1: #assumes format: "H1" and "C32"
        atom = atom[0]+'0'+atom[1]
    elif len(atom)<2:
        #print 'Error: len(atomName)<2'
		pass
    return atom

def addZeroToSimpleAtomList(simpleAtomList):
    returnList = []
    for atom in simpleAtomList:
        atom = addZeroToHNameAndCNameUnderTen(atom)
        returnList.append(atom)
    return returnList


def addDataToAtomsInMat(mat, atomData): #assumes data for all atoms in atomData.
    #print '-'
    for y, row in enumerate(mat):
        #print row
        for x, cell in enumerate(mat[y]):
            #print x, y
            if (y==0 and x>0) or (y>0 and x==0):
                #print cell, '==', mat[y][x]
                #print mat[y][x].replace('H0', 'H').replace('C0', 'C')
                data = atomData[mat[y][x].replace('H0', 'H').replace('C0', 'C')]
                if mat[y][x][0]== 'H':
                    st = '%.2f' % float(data)
                    #print st
                    data = st
                elif mat[y][x][0]== 'C':
                    st = '%.1f' % float(data)
                    #print st
                    data = st
                data = str(data)
                
                mat[y][x] = mat[y][x]+'('+data+')'
    #print '--'
    return mat

def fun_WriteMatrixFromCorrelations(H, C, cors, atomData):
    #H = sorted(['H2', 'H3', 'H1'])
    H =  addZeroToSimpleAtomList(H)
    H = sorted(H)
    #H.reverse()
    #print H
    #C = sorted(['C1', 'C3', 'C2'])
    C =  addZeroToSimpleAtomList(C)
    C = sorted(C)
    #C.reverse()
    #cors = [
    #    ['H1', 'C2', 'q'],
    #    ['H3', 'C3', 'q'],
    #    ['H1', 'C2', 'm'],
    #    ['H1', 'C3', 'm'],
    #    ['H1', 'C1', 'm'],
    #    ['H1', 'H2', 'c'],
    #    ]
    specTypes = ['H_C', 'H_H']
    #specTypes = ['H_C']
    datasets = [
        [H, C],
        [H, H],
        ]
    #print 'datasets', datasets, '\n'
    for specType, dataset in zip(specTypes, datasets):
        #print specType, dataset, '\n'
        #specType = 'H_C'
        atomX = dataset[0]
        #print 'atomX', atomX
        atomY = dataset[1]
        #print 'atomY', atomY
        #print 'dataset', dataset
        #print 'atomX', atomX
        #print 'atomY', atomY, '\n\n\n'

        dimX = len(atomX)+1
        dimY = len(atomY)+1
        #print dimX, dimY

        mat = ['' for i in range(dimY)]
        for e, l in enumerate(mat):
            mat[e] = ['' for i in range(dimX)]
        #print 'mat', mat

        mat[0]=[specType]+ atomX
        for n, row in enumerate(mat):
            if n > 0:
                #print 'n', n
                #print 'mat[n]', mat[n]
                #print 'mat[n][0]', mat[n][0]
                #print 'atomY[n-1]', atomY[n-1]
                #print 'ok'
                mat[n][0]=atomY[n-1]
                #print '-'


        #print 'mat', mat


        for y, row in enumerate(mat):
            for x, c in enumerate(mat[y]):
                if x>0 and y>0:
                    #print
                    #print x, y
                    #print mat
                    #print len(mat[0][x])
                    #print 'mat[0][x]', mat[0][x]
                    #print 'mat[y][0]', mat[y][0]
                    #print 'mat[0]', mat[0]
                    #print mat[0][x], mat[y][0]
                    if mat[0][x] == mat[y][0]:
                        
                        mat[y][x] = mat[y][x] + '*'
                    for cor in cors:
                        cor = [addZeroToHNameAndCNameUnderTen(cor[0]), addZeroToHNameAndCNameUnderTen(cor[1]), cor[2]]
                        #print 0, y
                        #print mat[0]
                        #print mat
                        #print mat[y]
                        #print cor, mat[0][x], mat[y][0]
                        #print '--'
                        if cor[0]==mat[0][x] and cor[1]==mat[y][0]:
                            #print '\t', cor
                            mat[y][x] = mat[y][x] + cor[2]
                #print x, y, mat[x][y]
                    
        #print mat, '\n'

        #print 'mat', mat
        mat = addDataToAtomsInMat(mat, atomData)

        export = ''
        for l in mat:
            #export += ', '.join(l)+'\n'
            #export += '\t'.join(l)+'\n'
            export += ';'.join(l)+'\n'

        #print export

        f = open(specType+'.csv', 'w')
        f.write(export)
        f.close()

        print 'Exported:', specType+'.csv'


if __name__ == '__main__':

    H = ['H2', 'H3', 'H1']
    C = ['C1', 'C3', 'C2']
    C = ['C1', 'C3', 'C2', 'C15']
    cors = [
            ['H1', 'C2', 'q'],
            ['H3', 'C3', 'q'],
            ['H1', 'C2', 'm'],
            ['H1', 'C3', 'm'],
            ['H1', 'C1', 'm'],
            ['H1', 'H2', 'c'],
            ]
    atomData={}
    atomData['H1'] = 333
    WriteMatrixFromCorrelations(H, C, cors, atomData)





