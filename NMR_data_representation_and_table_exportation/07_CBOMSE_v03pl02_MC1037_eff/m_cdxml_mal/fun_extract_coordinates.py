from bs4 import BeautifulSoup


def readFileAndMakeSoup(inName):
    #inName = 'testHMBC.xcmap'
    f = open(inName, 'r')
    data = ''.join(f.readlines())
    f.close()
    soup = BeautifulSoup(data, 'lxml')
    return soup


def getCoordinates(soup):
    coordinateList = []
    #soup = soup.html.body.cdxml.page.fragment
    soup = soup.html.body.cdxml.page
    
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
        d[c[0]] = [[c[1], c[2]]]
        d[c[0]] = [c[1], c[2]]
        #print c
    return d


def fun_extract_coordinates(inName):
    soup = readFileAndMakeSoup(inName)
    #print soup.html.body.cdxml.page.fragment
    coordinateList = getCoordinates(soup)
    d = makeDict(coordinateList)
    #print d
    return d
    


if __name__ == '__main__':
    inName = 'MC_mal.cdxml'
    fun_extract_coordinates(inName)

