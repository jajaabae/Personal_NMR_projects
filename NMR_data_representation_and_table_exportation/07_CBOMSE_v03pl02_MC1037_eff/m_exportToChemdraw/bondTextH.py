def test(NameOfH, cnt, rnd1, rnd2, coordDict):
    #print NameOfC
    #print cnt.NewAtomData[NameOfC][4]
    #print cnt.coordDict[cnt.NewAtomData[NameOfC][4]]
    try:
        #H_coords = cnt.coordDict[cnt.NewAtomData[NameOfH][4]]
        H_coords = coordDict[cnt.NewAtomData[NameOfH][4]]
        #print C_coords, rnd1, rnd2
        [rnd1, rnd2] = H_coords#[0]
        #print [rnd1, rnd2]
    except:
        pass
        #print 'error'
    #print s
    return [rnd1, rnd2]

def bondTextH(NameOfH, cnt, coordDict):
    import random
    import math
    [HPrefix, HPrefixNum, CPrefix, CPrefixNum] = cnt.getPrefixes()
    getppmText = cnt.getppmText[0]
    groups = cnt.groups
    grid = cnt.grid
    
    ppmText = getppmText(NameOfH, 2)
    #print ppmText
    #print '0', grid[0]
    #print NameOfH, groups[NameOfH]
    #rnd1 = random.choice(range(100, 200))
    #rnd2 = random.choice(range(100, 200))
    if not groups[NameOfH]==-1:
        try:
            #print '     --'
            #print NameOfH, groups[NameOfH], grid[groups[NameOfH]]
            [x,y]=grid[groups[NameOfH]]
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
    hydrogenLabel = '<t LabelJustification="Left" LabelAlignment="Below"><s font="3" size="10" color="0" face="96">'+NameOfH+ppmText+'</s></t>'
    #return '<n id="'+NameOfH.replace(HPrefix, HPrefixNum)+'" p="'+str(rnd1)+' '+str(rnd2)+'" Element="1" >'+hydrogenLabel+'</n>\n'

    [rnd1, rnd2] = test(NameOfH, cnt, rnd1, rnd2, coordDict)

    
    return '<n id="'+NameOfH.replace(HPrefix, HPrefixNum)+'" p="'+str(rnd1)+' '+str(rnd2)+'" Element="1" >'+hydrogenLabel+'</n>\n'
