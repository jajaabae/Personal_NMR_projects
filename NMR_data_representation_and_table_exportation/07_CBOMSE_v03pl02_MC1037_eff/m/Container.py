class Container():
    HPrefix = None
    HPrefixNum = None
    CPrefix = None
    CPrefixNum = None
    getppmText = None
    groups = None
    grid = None
    
    
    def fillContainer(self, HPrefix, HPrefixNum, CPrefix, CPrefixNum, getppmText, groups, grid,
                      #coordDict,
                      NewAtomData):
        Container.HPrefix = HPrefix
        Container.HPrefixNum = HPrefixNum
        Container.CPrefix = CPrefix
        Container.CPrefixNum = CPrefixNum
        Container.getppmText = [getppmText]
        Container.groups = groups
        Container.grid = grid
        #Container.coordDict = coordDict
        Container.NewAtomData = NewAtomData
        
        
    def getPrefixes(self):
        r = [
            Container.HPrefix,
            Container.HPrefixNum,
            Container.CPrefix,
            Container.CPrefixNum,
            ]
        #print r
        return r


