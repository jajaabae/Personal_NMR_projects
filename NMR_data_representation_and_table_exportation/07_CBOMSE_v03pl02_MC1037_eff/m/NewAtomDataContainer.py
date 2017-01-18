class NewAtomDataContainer():
    
    def nal_from_NewAtomData(self, NewAtomData):
        NAData_numToStr = {}
        NAData_strToNum = {}
        for numName in NewAtomData:
            #print numName, NewAtomData[numName]
            #strName = ''
            if numName[0] == 'C':
                try:
                    strName = NewAtomData[numName][5]
                    NAData_numToStr[numName] = str(strName)
                    NAData_strToNum[strName] = str(numName)
                except:
                    pass
            elif numName[0] == 'H':
                try:
                    strName = NewAtomData[numName][4]
                    NAData_numToStr[numName] = str(strName)
                    NAData_strToNum[strName] = str(numName)
                except:
                    pass
            else:
                pass
        itemsToDelete = []
        for n in NAData_numToStr:
            #print n, NAData_numToStr[n]
            if NAData_numToStr[n] == '':
                itemsToDelete += [n]
        for n in itemsToDelete:
            del NAData_numToStr[n]
        try:
            del NAData_strToNum['']
        except:
            pass
        NewAtomDataContainer.NAData_numToStr = NAData_numToStr
        NewAtomDataContainer.NAData_strToNum = NAData_strToNum
        
    def __init__(self, NewAtomData):
        NewAtomDataContainer.NewAtomData = NewAtomData
        self.nal_from_NewAtomData(NewAtomData)
        self.getStringsWithNumNamesAndViseVersa()


    def getStrNameFromNumName(self, numName):
        strName = None
        try:
            strName = NewAtomDataContainer.NAData_numToStr[numName]
        except:
            pass
        return strName

    def getNumNameFromStrName(self, strName):
        numName = None
        #print 
        #print strName
        #NewAtomDataContainer.NAData_strToNum[strName]
        try:
            #print 'test'
            numName = NewAtomDataContainer.NAData_strToNum[strName]
        except:
            pass
        return numName

    def getStringsWithNumNamesAndViseVersa(self):
        listOfNumNamesWithPartner = []
        listOfStrNamesWithPartner = []
        for n in NewAtomDataContainer.NAData_numToStr:
            #print n, NewAtomDataContainer.NAData_numToStr[n]
            if not n == '' and not NewAtomDataContainer.NAData_numToStr[n] == '':
                listOfNumNamesWithPartner += [n]
                listOfStrNamesWithPartner += [NewAtomDataContainer.NAData_numToStr[n]]
        #print listOfNumNamesWithPartner
        #print listOfStrNamesWithPartner
        NewAtomDataContainer.listOfNumNamesWithPartner = listOfNumNamesWithPartner
        NewAtomDataContainer.listOfStrNamesWithPartner = listOfStrNamesWithPartner

    def numHasPartner(self, strName):
        return strName in NewAtomDataContainer.listOfStrNamesWithPartner
        
    def strHasPartner(self, numName):
        return numName in NewAtomDataContainer.listOfNumNamesWithPartner











