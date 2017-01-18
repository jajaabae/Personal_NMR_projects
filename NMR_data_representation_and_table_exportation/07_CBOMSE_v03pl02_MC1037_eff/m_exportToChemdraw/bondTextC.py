def test(NameOfC, cnt, rnd1, rnd2, coordDict):
    #print NameOfC
    #print cnt.NewAtomData[NameOfC][4]
    #print cnt.coordDict[cnt.NewAtomData[NameOfC][4]]
    try:
        #C_coords = cnt.coordDict[cnt.NewAtomData[NameOfC][5]]
        C_coords = coordDict[cnt.NewAtomData[NameOfC][5]]
        #print C_coords, rnd1, rnd2
        [rnd1, rnd2] = C_coords#[0]
        #print [rnd1, rnd2]
    except:
        pass
    #print s
    return [rnd1, rnd2]


def bondTextC(NameOfC, cnt, coordDict):
    import random
    import math
    [HPrefix, HPrefixNum, CPrefix, CPrefixNum] = cnt.getPrefixes()
    getppmText = cnt.getppmText[0]
    groups = cnt.groups
    grid = cnt.grid
    #print getppmText
    
    ppmText = getppmText(NameOfC, 1)
    #print NameOfC, groups[NameOfC]
    #print NameOfC.replace(CPrefix, CPrefixNum)
    rnd1 = random.choice(range(100, 200))
    rnd2 = random.choice(range(100, 200))
    if not groups[NameOfC]==-1:
        try:
            #print '     --'
            #print grid[groups[NameOfC]]
            #print NameOfC, groups[NameOfC], grid[groups[NameOfC]]
            [x,y]=grid[groups[NameOfC]]
            #print x
            rnd1 = random.choice(range(int(math.ceil(x[0])), int(math.floor(x[1]))))
            rnd2 = random.choice(range(int(math.ceil(y[0])), int(math.floor(y[1]))))
        except:
            print 'Error in groups[NameOfH], from bondTextH(NameOfH) because of improper handeling of deleted bond'
            [x,y]=grid[0]
            rnd1 = random.choice(range(int(math.ceil(x[0])), int(math.floor(x[1]))))
            rnd2 = random.choice(range(int(math.ceil(y[0])), int(math.floor(y[1]))))
    else:
        #print '     --'
        #print NameOfH, groups[NameOfH], grid[groups[NameOfH]]
        [x,y]=grid[0]
        #print x
        rnd1 = random.choice(range(int(math.ceil(x[0])), int(math.floor(x[1]))))
        rnd2 = random.choice(range(int(math.ceil(y[0])), int(math.floor(y[1]))))
    #return '<n id="'+int1+'" p="'+str(rnd1)+' '+str(rnd2)+'" />'
    carbonLabel = '<t LabelJustification="Left" LabelAlignment="Below"><s font="3" size="10" color="0" face="96">'+NameOfC+'.'+ppmText+'</s></t>'
    #return '<n id="'+NameOfC.replace(CPrefix, CPrefixNum)+'" p="'+str(rnd1)+' '+str(rnd2)+'" >'+carbonLabel+'</n>\n'

    #print cnt.coordDict
    #print NameOfC, cnt.coordDict['N'], rnd1
    [rnd1, rnd2] = test(NameOfC, cnt, rnd1, rnd2, coordDict)
    
    text = '<n id="'+NameOfC.replace(CPrefix, CPrefixNum)+'" p="'+str(rnd1)+' '+str(rnd2)+'" >'+carbonLabel+'</n>\n'
    return text
