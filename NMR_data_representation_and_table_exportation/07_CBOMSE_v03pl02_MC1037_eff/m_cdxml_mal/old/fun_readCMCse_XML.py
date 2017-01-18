from bs4 import BeautifulSoup






def readFileAndMakeSoup(inName):
    #inName = 'testHMBC.xcmap'
    f = open(inName, 'r')
    data = ''.join(f.readlines())
    f.close()

    soup = BeautifulSoup(data, 'lxml')
    return soup


def readCorList(soup):


    corList = []
    #print len(soup.find_all('peakgroup'))
    for PeakGroup in soup.find_all('peakgroup'):
        if len(PeakGroup.find_all('cortype')) == len(PeakGroup.find_all('atomindex')):
            for typeName, ints in zip(PeakGroup.find_all('cortype'), PeakGroup.find_all('atomindex')):
                cor = []
                for anInt in ints.find_all('int'):
                    cor.append(str(int(anInt.text)+1))
                #print cor
                cor.append(typeName.text)
                corList.append(cor)
        else:
            print 'ERROR'
    #print corList
    return corList

#corList = readCorList(soup)
#print len(corList)
#print corList


def getProtons(soup):
    protons = {}
    for proton in soup.find_all('protonprops'):
        #print proton
        #print 'ordinal', proton.ordinal.text
        ordinal = proton.ordinal.text
        number = str(int(proton.ordinal.text)+1)
        #print 'symbol', proton.symbol.text
        symbol = proton.symbol.text
        name = symbol+number
        #print 'chemshift', proton.chemshift.text
        chemshift = proton.chemshift.text
        #print 'multipletstruct', proton.multipletstruct.text
        multipletstruct = proton.multipletstruct.text
        #print 'useratomname', proton.useratomname.text
        useratomname = ''
        try:
            useratomname = proton.useratomname.text
        except:
            pass
        usercomment = 'none'
        if not proton.usercomment == None:
        #    print 'userComment', proton.usercomment.text
            usercomment = proton.usercomment.text
        #print
        protons[name]=[symbol, number, chemshift, multipletstruct, useratomname, usercomment]
    return protons
#atomData={}
#atomData.update(getProtons())


#XNucPropsC
def getXnucC(soup):
    carbons = {}
    for xnuc in soup.find_all('xnucpropsc'):
        #print xnuc
        #"""
        #print 'ordinal', xnuc.ordinal.text
        ordinal = xnuc.ordinal.text
        number = str(int(xnuc.ordinal.text)+1)
        #print 'symbol', xnuc.symbol.text
        symbol = xnuc.symbol.text
        name = symbol+number
        #print 'chemshift', xnuc.chemshift.text
        chemshift = xnuc.chemshift.text
        #print 'multipletstruct', xnuc.multipletstruct.text
        multipletstruct = xnuc.multipletstruct.text
        #print 'numh', xnuc.numh.text
        numh = xnuc.numh.text
        #"""
        useratomname = ''
        try:
            useratomname = xnuc.useratomname.text
        except:
            pass
        carbons[name] = [symbol, number, chemshift, multipletstruct, numh, useratomname]
        
    return carbons
#atomData.update(getXnucC())
#print getXnucC()

#XNucPropsN
#XNucPropsO


def getAtomsListed(atomData):
    HList = []
    CList = []
    for atom in atomData:
        if atomData[atom][0]=='H':
            #print atomData[atom][1]
            HList.append(atomData[atom][1])
        elif atomData[atom][0]=='C':
            #print atomData[atom][1]
            CList.append(atomData[atom][1])
    return HList, CList
#[HList, CList] = getAtomsListed(atomData)




def getOldAtomDataFormat(atomData):
    OldAtomDataFormat = {} 
    for atom in atomData:
        #print atomData[atom][2]
        OldAtomDataFormat[atom] = atomData[atom][2]
    return OldAtomDataFormat


def fun_readCMCse_XML(inName):
#def getDataFromFile(inName):
    #inName = 'testHMBC.xcmap'
    soup = readFileAndMakeSoup(inName)
    
    corList = readCorList(soup)
    
    atomData={}
    atomData.update(getProtons(soup))
    atomData.update(getXnucC(soup))
    
    [HList, CList] = getAtomsListed(atomData)
    OldAtomDataFormat = getOldAtomDataFormat(atomData)
    
    return atomData, corList, HList, CList, OldAtomDataFormat



if __name__ == '__main__':
    inName = 'MC1045_restart.xcmap'
    inName = 'TEST.xcmap'

    atomData, corList, HList, CList, OldAtomDataFormat = getDataFromFile(inName)
    #print OldAtomDataFormat
    #"""
    print len(corList)
    print corList
    print 
    print HList
    print CList
    print 
    print atomData
    #"""


















