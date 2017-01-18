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
    """
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
    #"""
    #print corList
    return corList


def test(soup):
    corList = []
    soup = soup.html.body.cdxml.page.fragment
    print 'b:', len(soup.find_all('b'))
    print 'n:', len(soup.find_all('n'))
    print 't:', len(soup.find_all('t'))
    print 's:', len(soup.find_all('s'))

    for s in soup.find_all('s'):
        #print
        #print s
        #print s.text
        #print s.parent.parent
        #print s.parent.parent.p
        #print s.parent.parent.text
        #print s.parent.parent.name
        try:
            [x,y] = s.parent.parent['p'].split(' ')
            name = str(s.text)
            out = [name, x, y]
            print out
        except:
            #print 'Error'
            pass

        
    
    """
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
    #"""
    #print corList
    return corList



def getCoordinates(soup):
    coordinateList = []
    soup = soup.html.body.cdxml.page.fragment
    
    for s in soup.find_all('s'):
        try:
            [x,y] = s.parent.parent['p'].split(' ')
            name = str(s.text)
            out = [name, x, y]
            #print out
            coordinateList += [out]
        except:
            #print 'Error'
            pass
    return coordinateList

def makeDict(coordinateList):
    d = {}
    for c in coordinateList:
        #print c
        #print c[0], [c[1], c[2]]
        d[c[0]] = [c[1], c[2]]
    return d


def fun_readCMCse_XML(inName):
    soup = readFileAndMakeSoup(inName)
    #print soup
    #print soup.html.body.cdxml.page.fragment
    #corList = readCorList(soup)

    #corList = test(soup)
    coordinateList = getCoordinates(soup)
    #print coordinateList
    #for c in coordinateList:
    #    print c
    d = makeDict(coordinateList)
    print d
    

    



if __name__ == '__main__':
    inName = 'MC_mal.cdxml'
    fun_readCMCse_XML(inName)

