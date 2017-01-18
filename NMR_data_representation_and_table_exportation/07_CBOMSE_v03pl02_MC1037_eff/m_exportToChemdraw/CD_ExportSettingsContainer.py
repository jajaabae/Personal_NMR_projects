class CD_ExportSettingsContainer():
    def init_stdDict(**keywords):
        d = keywords
        return d
    
    stdDict = init_stdDict(
            bonds = ['CH', 'HH', 'CC'],
            correlations = 'ctrqm', #ctnrmq 
            cor_colors = init_stdDict(
                        c = 'cyan',
                        t = 'green',
                        r = 'red',
                        #n = 'black',
                        ##q = 'magenta',
                        m = 'black',
                        ),
            bond_colors = init_stdDict(
                        CC = 'blue',
                        CH = 'magenta',
                        HH = 'cyan',
                        ),
            explanatoryBondColor = True,
            writeCorrelations = True,
            #lineType = ???
            )

    cd_color_lookupTable = init_stdDict(
        black = 0,
        white = 1,
        white2 = 2,
        black2 = 3,
        red = 4,
        yellow = 5,
        green = 6,
        cyan = 7,
        blue = 8,
        magenta = 9,
        )
    
    def __init__(self, **keywords):
        self.keywords = CD_ExportSettingsContainer.stdDict
        self.keywords.update(keywords)

    def getCorColor(self, corType):
        return self.cd_color_lookupTable[self.keywords['cor_colors'][corType]]
    def getBondColor(self, BondType):
        return self.cd_color_lookupTable[self.keywords['bond_colors'][BondType]]
        


"""
            cor_colors = init_stdDict(
                        c = 'yellow',
                        t = 'yellow',
                        r = 'red',
                        #n = 'black',
                        ##q = 'magenta',
                        m = 'black',
                        ),
            #"""
