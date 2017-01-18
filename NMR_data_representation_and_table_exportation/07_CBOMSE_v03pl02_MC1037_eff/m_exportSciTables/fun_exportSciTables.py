from m.mfi import imp
exec(imp())


def hsqcCor(c, h):
    corTest = False
    for cor in correlations:
        if 'q' in cor:
            if h in cor and c in cor:
                corTest = True
    return corTest

def getRoundedPpmText(inPpmText, decimals):
    #ppmText = ''
    ppmText = "{0:.{1}f}".format(float(inPpmText), decimals)
    return ppmText

def getCText(cName, NewAtomData):
    returnString = ''
    for d in NewAtomData:
        if NewAtomData[d][5]==cName and not cName == '' and NewAtomData[d][0]=='C':
            ppmC = getRoundedPpmText(NewAtomData[d][2], 1)
            if ppmC == 'nan':
                #ppmC = '-'
                ppmC = defaultStringContainer.defaultString
            returnString += ppmC
    return returnString

def getHText(hName, NewAtomData):
    returnString = ''
    #print hName
    for d in NewAtomData:
        if NewAtomData[d][4]==hName and not hName == '' and NewAtomData[d][0]=='H':
            ppmH = getRoundedPpmText(NewAtomData[d][2], 2)
            if ppmH == 'nan':
                #ppmH = '-'
                ppmH = defaultStringContainer.defaultString
            returnString += ppmH
    if returnString =='':
        #returnString='-'
        returnString = defaultStringContainer.defaultString
    return returnString

def getHNumberedNameFromHName(hName, NewAtomData):
    HNumberedName = ''
    for d in NewAtomData:
        if NewAtomData[d][4]==hName and not hName == '' and NewAtomData[d][0]=='H':
            HNumberedName = ''.join([NewAtomData[d][0], NewAtomData[d][1]])
    return HNumberedName

def getCNumberedNameFromCName(hName, NewAtomData):
    HNumberedName = ''
    for d in NewAtomData:
        #print NewAtomData[d]
        if NewAtomData[d][5]==hName and not hName == '' and NewAtomData[d][0]=='C':
            HNumberedName = ''.join([NewAtomData[d][0], NewAtomData[d][1]])
    return HNumberedName



def getHNameFromHNumberedName(HNumberedName, NewAtomData):
    HName = ''
    for d in NewAtomData:
        #if NewAtomData[d][4]==HNumberedName and not HNumberedName == '' and NewAtomData[d][0]=='H':
        if ''.join([NewAtomData[d][0], NewAtomData[d][1]])==HNumberedName and not HNumberedName == '' and HNumberedName[0]=='H':
            #HName = ''.join([NewAtomData[d][0], NewAtomData[d][1]])
            HName = NewAtomData[d][4]
    return HName




def getCorrelationsFromNumberedName(HNumberedName, corType, correlations):
    cosyCorrelations = []
    for cor in correlations:
        corCopy = list(cor)
        if corType in cor and HNumberedName in cor:
            corCopy.remove(corType)
            corCopy.remove(HNumberedName)
            cosyCorrelations+=[corCopy[0]]
    return cosyCorrelations

def formatOneWayCorrelationList(corrList):
    corrString = ''
    #from fun_splitListIntoSingleAndMultipleOccurences import splitListIntoSingleAndMultipleOccurences
    i_fsf('m_exportSciTables.splitListIntoSingleAndMultipleOccurences')
    singles, multiple = splitListIntoSingleAndMultipleOccurences(corrList)

    #multiple = [x+'r' for x in multiple]
    #singles = [x+'s' for x in singles]

    both = singles + multiple
    both.sort()
    corrString += ', '.join(both)
    return corrString

def formatDualWayCorrelationList(corrList):
    corrString = ''
    #from fun_splitListIntoSingleAndMultipleOccurences import splitListIntoSingleAndMultipleOccurences
    i_fsf('m_exportSciTables.splitListIntoSingleAndMultipleOccurences')
    singles, multiple = splitListIntoSingleAndMultipleOccurences(corrList)
    
    #multiple = [x+'r' for x in multiple]
    singles = [x+'s' for x in singles]

    both = singles + multiple
    both.sort()
    corrString += ', '.join(both)
    return corrString
    
def getCosyCorrelations(hName, NewAtomData, correlations):
    returnString = ''
    HNumberedName = getHNumberedNameFromHName(hName, NewAtomData)
    corrList = []
    corrList += getCorrelationsFromNumberedName(HNumberedName, 'c', correlations)
    #corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, NewAtomData)
    c_or_h = 'H'
    corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, c_or_h, NewAtomData)
    returnString += formatDualWayCorrelationList(corrList)
    if returnString =='':
        #returnString='-'
        returnString = defaultStringContainer.defaultString
    return returnString

def getTocsyCorrelations(hName, NewAtomData, correlations):
    returnString = ''
    HNumberedName = getHNumberedNameFromHName(hName, NewAtomData)
    corrList = []
    corrList += getCorrelationsFromNumberedName(HNumberedName, 't', correlations)
    #corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, NewAtomData)
    c_or_h = 'H'
    corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, c_or_h, NewAtomData)
    returnString += formatDualWayCorrelationList(corrList)
    if returnString =='':
        #returnString='-'
        returnString = defaultStringContainer.defaultString
    return returnString

def getHsqcCorrelations(hName, NewAtomData, correlations):
    returnString = ''
    HNumberedName = getHNumberedNameFromHName(hName, NewAtomData)
    corrList = []
    corrList += getCorrelationsFromNumberedName(HNumberedName, 'q', correlations)
    c_or_h = 'C'
    corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, c_or_h, NewAtomData)
    returnString += formatOneWayCorrelationList(corrList)
    if returnString =='':
        #returnString='-'
        returnString = defaultStringContainer.defaultString
    return returnString

def getHmbcCorrelations(hName, NewAtomData, correlations):
    returnString = ''
    HNumberedName = getHNumberedNameFromHName(hName, NewAtomData)
    corrList = []
    corrList += getCorrelationsFromNumberedName(HNumberedName, 'm', correlations)
    #corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, NewAtomData)
    c_or_h = 'C'
    corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, c_or_h, NewAtomData)
    returnString += formatOneWayCorrelationList(corrList)
    if returnString =='':
        #returnString='-'
        returnString = defaultStringContainer.defaultString
    return returnString

def getRoesyCorrelations(hName, NewAtomData, correlations, typeOfRoesyCorrelations):
    returnString = ''
    HNumberedName = getHNumberedNameFromHName(hName, NewAtomData)
    corrList = []
    cor_cont=correlationContainer()
    
    
    
    #onlyPureRoesyCorrelations = cor_cont.onlyPureRoesyCorrelations
    #if onlyPureRoesyCorrelations:
    #    corrList += getCorrelationsFromNumberedName(HNumberedName, 'r', reducedCorrelations)
    #else:
    #    corrList += getCorrelationsFromNumberedName(HNumberedName, 'r', correlations)
    
    if typeOfRoesyCorrelations == 'external':
        reducedCorrelations = cor_cont.correlations_roesyNoTocsyOrCosy
        corrList += getCorrelationsFromNumberedName(HNumberedName, 'r', reducedCorrelations)
    elif typeOfRoesyCorrelations == 'internal':
        internalCorrelations = cor_cont.correlations_internal_roesy
        corrList += getCorrelationsFromNumberedName(HNumberedName, 'r', internalCorrelations)
    elif typeOfRoesyCorrelations == 'all':
        corrList += getCorrelationsFromNumberedName(HNumberedName, 'r', correlations)
    else:
        print 'Error: getRoesyCorrelations()'
    
    #print '******************************************'
    #print reducedCorrelations
    #print corrList
    #print '******************************************'
    
    #corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, NewAtomData)
    c_or_h = 'H'
    corrList = replaceCorrsWithFullNamesOrPpmValues(corrList, c_or_h, NewAtomData)
    returnString += formatDualWayCorrelationList(corrList)
    if returnString =='':
        #returnString='-'
        returnString = defaultStringContainer.defaultString
    return returnString

def get_data_from_md_object(md_object, atom_name, data_name):
    data_string = ''
    try:
        data_string = md_object.Carbons[atom_name].export_strings[data_name]
        #print inLine[1], md_object.Carbons[inLine[1]].data['Amino Acid']
    except:
        pass
    try:
        data_string = md_object.Hydrogens[atom_name].export_strings[data_name]
    except:
        pass
    return data_string

def getCHText(inLine, NewAtomData, correlations, md_object, includeExtraColumns):
    line = ''
    line += inLine[0]
    line+='\t'
    if not inLine[1] == '':
        line += "'"+inLine[1].split(' ')[1]
    elif not inLine[2] == '' and 'NH' in inLine[2]:
        line += "'"+inLine[2].split(' ')[1]

    #line+='\t'
    #line+=getCNumberedNameFromCName(inLine[2], NewAtomData) #error
    ##line+=inLine[2]
    
    line+='\t'
    line+=getCText(inLine[1], NewAtomData)#C


    #HSQC_pos_neg
    line += '\t'
    line += get_data_from_md_object(md_object, inLine[1], 'HSQC_pos_neg')
    #print get_data_from_md_object(md_object, inLine[2], 'HSQC_pos_neg')
    

    #line+='\t'
    #line+=getHNumberedNameFromHName(inLine[1], NewAtomData) #error
    ##line+=inLine[1]
    
    line+='\t'
    line+=getHText(inLine[2], NewAtomData)#H


    #Multiplicity
    line += '\t'
    line += get_data_from_md_object(md_object, inLine[2], 'mult_str')
    #print get_data_from_md_object(md_object, inLine[2], 'mult_str'),

    #Number of Hydrogens
    line += '\t'
    line += get_data_from_md_object(md_object, inLine[2], 'number_of_hydrogens')
    #print get_data_from_md_object(md_object, inLine[2], 'number_of_hydrogens'),

   
    line+='\t'
    line+=getCosyCorrelations(inLine[2], NewAtomData, correlations)#COSY
    line+='\t'
    line+=getTocsyCorrelations(inLine[2], NewAtomData, correlations)#TOCSY
    line+='\t'
    line+=getHsqcCorrelations(inLine[2], NewAtomData, correlations)#HSQC
    line+='\t'
    line+=getHmbcCorrelations(inLine[2], NewAtomData, correlations)#HMBC
    line+='\t'
    typeOfRoesyCorrelations = 'external'
    line+=getRoesyCorrelations(inLine[2], NewAtomData, correlations, typeOfRoesyCorrelations)#pure_ROESY
    line+='\t'
    typeOfRoesyCorrelations = 'internal'
    line+=getRoesyCorrelations(inLine[2], NewAtomData, correlations, typeOfRoesyCorrelations)#internal_ROESY
    line+='\t'
    typeOfRoesyCorrelations = 'all'
    line+=getRoesyCorrelations(inLine[2], NewAtomData, correlations, typeOfRoesyCorrelations)#std_ROESY


    if includeExtraColumns:
        #mult_str_for_copy
        line+='\t'
        mult_str_for_copy = getHText(inLine[2], NewAtomData)+' ppm '+get_data_from_md_object(md_object, inLine[2], 'partial_mult_str_for_copy')
        if not mult_str_for_copy == getHText(inLine[2], NewAtomData)+' ppm ':
            line += mult_str_for_copy
        
        #carbon_str_for_copy
        line+='\t'
        carbon_str = getCText(inLine[1], NewAtomData)+' ppm ('+get_data_from_md_object(md_object, inLine[1], 'HSQC_pos_neg').replace("'", '')+')'
        if not carbon_str == ' ppm ()':
            line+= carbon_str
        
        #C-name
        line+='\t'
        line+=inLine[1] #C
        
        #H-name
        line+='\t'
        line+=inLine[2] #H
        
    
    return line

def printInTableFormat(Carbons, Hydrogens, NewAtomData, correlations, tableFormat, md_object): #includeExtraColumns, print_table_in_shell):
    includeExtraColumns=True
    #includeExtraColumns=False
    print_table_in_shell = True
    #print_table_in_shell = False
    
    lines = []
    #startLine = 'Amino acid	Atom name	c_num	C	h_num	H	COSY	TOCSY	HSQC	HMBC	ROESY'
    #startLine = 'Amino acid	Atom name	C	HSQC_+/-	H	Multip.	N(H)	COSY	TOCSY	HSQC	HMBC	ROESY	mult_str_for_copy	carbon_str	C-name	H-name'
    startLine = 'Amino acid	Atom name	C	HSQC_+/-	H	Multip.	N(H)	COSY	TOCSY	HSQC	HMBC	ex_ROESY	in_ROESY	all_ROESY'
    if includeExtraColumns:
        startLine += '	mult_str_for_copy	carbon_str	C-name	H-name'
    lines.append(startLine)
    for line in tableFormat:
        lines.append(getCHText(line, NewAtomData, correlations, md_object, includeExtraColumns))

    f = open('exportedSciTable.csv', 'w')
    for l in lines:
        f.write(l.replace('\t', ';')+'\n')
        if print_table_in_shell:
            print l
    f.close()

def getPrintTableFormat():
    table = [
            ['Leu1',	'CLeu1 1',	''],
            ['',	'CLeu1 2',	'HLeu1 2'],
            ['',	'',	'HLeu1 2-NH'],
            ['',	'CLeu1 3',	'HLeu1 3a'],
            ['',	'',	'HLeu1 3b'],
            ['',	'CLeu1 4',	'HLeu1 4'],
            ['',	'CLeu1 5a',	'HLeu1 5a'],
            ['',	'CLeu1 5b',	'HLeu1 5b'],
            ['Leu2',	'CLeu2 1',	''],
            ['',	'CLeu2 2',	'HLeu2 2'],
            ['',	'',	'HLeu2 2-NH'],
            ['',	'CLeu2 3',	'HLeu2 3a'],
            ['',	'',	'HLeu2 3b'],
            ['',	'CLeu2 4',	'HLeu2 4'],
            ['',	'CLeu2 5a',	'HLeu2 5a'],
            ['',	'CLeu2 5b',	'HLeu2 5b'],
            ['Me-Asp3',	'CMe-Asp3 1',	'HMe-Asp3 1'],
            ['',	'CMe-Asp3 2',	'HMe-Asp3 2'],
            ['',	'',	'HMe-Asp3 2-NH'],
            ['',	'CMe-Asp3 3',	'HMe-Asp3 3'],
            ['',	'CMe-Asp3 3-Me',	'HMe-Asp3 3-Me'],
            ['',	'CMe-Asp3 4',	'HMe-Asp3 4'],
            ['Arg4',	'CArg4 1',	''],
            ['',	'CArg4 2',	'HArg4 2'],
            ['',	'',	'HArg4 2-NH'],
            ['',	'CArg4 3',	'HArg4 3a'],
            ['',	'',	'HArg4 3b'],
            ['',	'CArg4 4',	'HArg4 4a'],
            ['',	'',	'HArg4 4b'],
            ['',	'CArg4 5',	'HArg4 5a'],
            #['',	'',	'HArg4 5b'],
            ['',	'',	'HArg4 5-NH'],
            ['Adda5',	'CAdda5 1',	''],
            ['',	'CAdda5 2',	'HAdda5 2'],
            ['',	'CAdda5 2-Me',	'HAdda5 2-Me'],
            ['',	'CAdda5 3',	'HAdda5 3'],
            ['',	'',	'HAdda5 3-NH'],
            ['',	'CAdda5 4',	'HAdda5 4'],
            ['',	'CAdda5 5',	'HAdda5 5'],
            ['',	'CAdda5 6',	''],
            ['',	'CAdda5 6-Me',	'HAdda5 6-Me'],
            ['',	'CAdda5 7',	'HAdda5 7'],
            ['',	'CAdda5 8',	'HAdda5 8'],
            ['',	'CAdda5 8-Me',	'HAdda5 8-Me'],
            ['',	'CAdda5 9',	'HAdda5 9'],
            ['',	'CAdda5 9-OMe',	'HAdda5 9-OMe'],
            ['',	'CAdda5 10',	'HAdda5 10a'],
            ['',	'',	'HAdda5 10b'],
            ['',	'CAdda5 11',	''],
            ['',	'CAdda5 12',	'HAdda5 12'],
            ['',	'CAdda5 13',	'HAdda5 13'],
            ['',	'CAdda5 14',	'HAdda5 14'],
            ['Glu6',	'CGlu6 1',	''],
            ['',	'CGlu6 2',	'HGlu6 2'],
            ['',	'',	'HGlu6 2-NH'],
            ['',	'CGlu6 3',	'HGlu6 3a'],
            ['',	'',	'HGlu6 3b'],
            ['',	'CGlu6 4',	'HGlu6 4a'],
            ['',	'',	'HGlu6 4b'],
            ['',	'CGlu6 5',	''],
            ['Mdha7',	'CMdha7 1',	''],
            ['',	'CMdha7 2',	''],
            ['',	'CMdha7 2-N-Me',	'HMdha7 2-N-Me'],
            ['',	'CMdha7 3',	'HMdha7 3a'],
            ['',	'',	'HMdha7 3b'],
    ]
    return table





### replace 'xnn' with full names ###
def getNameFromNumberedName(numberedName, NewAtomData):
    NN = numberedName
    boolRemFirst = True
    try:
        if numberedName[0]=='H':
            #print numberedName, NewAtomData[numberedName][4]
            NN = NewAtomData[numberedName][4]
            if boolRemFirst:
                NN = NN[1:]
        elif numberedName[0]=='C':
            #print numberedName, NewAtomData[numberedName][5]
            NN = NewAtomData[numberedName][5]
            if boolRemFirst:
                NN = NN[1:]
        else:
            print 'error:', numberedName
    except:
        pass
    return NN


def replaceCorrsWithFullNamesOrPpmValues(corrList, c_or_h, NewAtomData):
    retList = []
    c = ReplaceNamesBooleanContainer()
    if c.B == True:
        if not c.convertKvownNamesToNumbers: # replace with full names
            for i in corrList:
                numberedName = i
                retList.append(getNameFromNumberedName(numberedName, NewAtomData))
        else: # replace with ppm values
            for i in corrList:
                numberedName = i
                #retList.append(getNameFromNumberedName(numberedName, NewAtomData))
                #print ppmValue(numberedName, NewAtomData)
                if c_or_h == 'H':
                    retList.append( ppmValueH(numberedName, NewAtomData))
                elif c_or_h == 'C':
                    retList.append( ppmValueC(numberedName, NewAtomData))
                else:
                    print "error: replaceCorrsWithFullNamesOrPpmValues"
                
        #print retList
    else:
        retList = corrList
    return retList

class ReplaceNamesBooleanContainer():
    B = None
    convertKvownNamesToNumbers = None
    def setBool(self, convertKvownNames, convertKvownNamesToNumbers):
        ReplaceNamesBooleanContainer.B = convertKvownNames
        ReplaceNamesBooleanContainer.convertKvownNamesToNumbers = convertKvownNamesToNumbers


def ppmValueH(hName, NewAtomData):
    returnString = ''
    for d in NewAtomData:
        #print hName, d, NewAtomData[d]
        #if NewAtomData[d][4]==hName and not hName == '' and NewAtomData[d][0]=='H':
        if hName == d and not hName == '':
            #print hName, d, NewAtomData[d]
            ppmH = getRoundedPpmText(NewAtomData[d][2], 2)
            if ppmH == 'nan':
                ppmH = '-'
            returnString += ppmH
    if returnString =='':
        returnString='-'
    return returnString

def ppmValueC(cName, NewAtomData):
    returnString = ''
    for d in NewAtomData:
        if cName == d and not cName == '':
            #print hName, d, NewAtomData[d]
            ppmC = getRoundedPpmText(NewAtomData[d][2], 1) #!!!!!!!!!!!!!
            #print ppmC
            
            if ppmC == 'nan':
                ppmC = '-'
            returnString += ppmC
    if returnString =='':
        returnString='-'
    return returnString

class correlationContainer():
    correlations_roesyNoTocsyOrCosy=[]
    def generate_reduced_correlations(self, correlations):
        cosyOrTocsy_cors = []
        for c in correlations:
            if c[2]=='c' or c[2]=='t':
                #print c
                cosyOrTocsy_cors.append(c)
        pureRoesy = []
        for c in correlations:
            if c[2]=='r' and self.noneTocsyOrCosyCorrelations(c, correlations):
            #if c[2]=='r' and c not in cosyOrTocsy_cors:
                #print c
                pureRoesy.append(c)
            #else:
            #    print c
        #print pureRoesy
        correlationContainer.correlations_roesyNoTocsyOrCosy = pureRoesy
        
    def noneTocsyOrCosyCorrelations(self, cor, correlations):
        #existInCosyOrRoesy = False
        notInCosyOrRoesy = True
        for c in correlations:
            if ( c[2]=='c' or c[2]=='t' ) and ( c[0:2]==cor[0:2] or c[0:2]==list(reversed(cor[0:2])) ):
                #existInCosyOrRoesy=True
                notInCosyOrRoesy = False
                #print c, c[0], getHText(c[0], tmpContainer.NewAtomData)
                #print c, c[0], getHText(getHNameFromHNumberedName(c[0], tmpContainer.NewAtomData), tmpContainer.NewAtomData)
                #print getHText(getHNameFromHNumberedName(c[0], tmpContainer.NewAtomData), tmpContainer.NewAtomData), getHText(getHNameFromHNumberedName(c[1], tmpContainer.NewAtomData), tmpContainer.NewAtomData)
                
    #    print correlations
    #    #return reducedCorrelations
        #return existInCosyOrRoesy
        return notInCosyOrRoesy


    def generate_internal_correlations(self, correlations):
        cosyOrTocsy_cors = []
        for c in correlations:
            if c[2]=='c' or c[2]=='t':
                cosyOrTocsy_cors.append(c)
        internalRoesy = []
        for c in correlations:
            if c[2]=='r' and self.isInTocsyOrCosyCorrelations(c, correlations):
                internalRoesy.append(c)
        correlationContainer.correlations_internal_roesy = internalRoesy
        
    def isInTocsyOrCosyCorrelations(self, cor, correlations):
        isInCosyOrRoesy = False
        for c in correlations:
            if ( c[2]=='c' or c[2]=='t' ) and ( c[0:2]==cor[0:2] or c[0:2]==list(reversed(cor[0:2])) ):
                isInCosyOrRoesy = True
        return isInCosyOrRoesy


class defaultStringContainer():
    #defaultString = '-'
    defaultString = "'-"

class tmpContainer():
    NewAtomData=None
    def __init__(self, NewAtomData):
        tmpContainer.NewAtomData = NewAtomData



#def exportSciTable(Carbons, Hydrogens, NewAtomData, correlations):
#    printInTableFormat(Carbons, Hydrogens, NewAtomData, correlations, getPrintTableFormat())
def fun_exportSciTables(Carbons, Hydrogens, NewAtomData, correlations, convertKvownNames, convertKvownNamesToNumbers, onlyPureRoesyCorrelations, md_object):
    tmpContainer(NewAtomData)
    
    cor_cont = correlationContainer()
    cor_cont.generate_reduced_correlations(correlations)
    cor_cont.generate_internal_correlations(correlations)
    correlationContainer.onlyPureRoesyCorrelations=onlyPureRoesyCorrelations
    
    #print 'cor_cont.correlations_roesyNoTocsyOrCosy: ', cor_cont.correlations_roesyNoTocsyOrCosy
    tmpAllRoesy=[]
    for c in correlations:
        if c[2]=='r':
            tmpAllRoesy.append(c)
    #print
    #print tmpAllRoesy
    #print 
    
    c = ReplaceNamesBooleanContainer()
    #c.setBool(False)
    #c.setBool(True)
    c.setBool(convertKvownNames, convertKvownNamesToNumbers)
    #print 'c.B', c.B
    #print getNameFromNumberedName('C20', NewAtomData)
    #print getNameFromNumberedName('H15', NewAtomData)

    
    print len(correlationContainer.correlations_roesyNoTocsyOrCosy)
    print len(tmpAllRoesy)

    printInTableFormat(Carbons, Hydrogens, NewAtomData, correlations, getPrintTableFormat(), md_object)







if __name__ == '__main__':
    correlations = [['H10', 'C16', 'q'], ['H8', 'C15', 'q'], ['H9', 'C14', 'q'], ['H11', 'C11', 'q'], ['H12', 'C18', 'q'], ['H14', 'C18', 'q'], ['H13', 'C17', 'q'], ['H15', 'C12', 'q'], ['H23', 'C19', 'q'], ['H18', 'C21', 'q'], ['H16', 'C22', 'q'], ['H19', 'C25', 'q'], ['H20', 'C23', 'q'], ['H21', 'C24', 'q'], ['H17', 'C26', 'q'], ['H24', 'C20', 'q'], ['H22', 'C32', 'q'], ['H27', 'C27', 'q'], ['H29', 'C31', 'q'], ['H28', 'C31', 'q'], ['H35', 'C29', 'q'], ['H38', 'C30', 'q'], ['H37', 'C39', 'q'], ['H44', 'C30', 'q'], ['H41', 'C29', 'q'], ['H30', 'C34', 'q'], ['H32', 'C34', 'q'], ['H39', 'C38', 'q'], ['H40', 'C47', 'q'], ['H33', 'C36', 'q'], ['H36', 'C36', 'q'], ['H47', 'C44', 'q'], ['H31', 'C33', 'q'], ['H34', 'C35', 'q'], ['H43', 'C35', 'q'], ['H42', 'C37', 'q'], ['H48', 'C41', 'q'], ['H48', 'C40', 'q'], ['H49', 'C43', 'q'], ['H49', 'C42', 'q'], ['H45', 'C45', 'q'], ['H46', 'C46', 'q'], ['H11', 'C12', 'm'], ['H11', 'C47', 'm'], ['H9', 'C31', 'm'], ['H8', 'C10', 'm'], ['H15', 'C47', 'm'], ['H28', 'C19', 'm'], ['H29', 'C19', 'm'], ['H24', 'C19', 'm'], ['H28', 'C14', 'm'], ['H29', 'C14', 'm'], ['H28', 'C10', 'm'], ['H29', 'C10', 'm'], ['H28', 'C6', 'm'], ['H29', 'C6', 'm'], ['H22', 'C3', 'm'], ['H22', 'C9', 'm'], ['H45', 'C2', 'm'], ['H46', 'C1', 'm'], ['H45', 'C27', 'm'], ['H46', 'C28', 'm'], ['H47', 'C33', 'm'], ['H40', 'C13', 'm'], ['H40', 'C12', 'm'], ['H40', 'C11', 'm'], ['H47', 'C19', 'm'], ['H47', 'C12', 'm'], ['H21', 'C3', 'm'], ['H12', 'C7', 'm'], ['H14', 'C7', 'm'], ['H11', 'C22', 'm'], ['H23', 'C10', 'm'], ['H14', 'C9', 'm'], ['H1', 'H19', 'c'], ['H3', 'H20', 'c'], ['H7', 'H26', 'c'], ['H19', 'H1', 'c'], ['H20', 'H3', 'c'], ['H21', 'H2', 'c'], ['H18', 'H5', 'c'], ['H16', 'H4', 'c'], ['H17', 'H6', 'c'], ['H4', 'H16', 'c'], ['H6', 'H17', 'c'], ['H5', 'H18', 'c'], ['H11', 'H13', 'c'], ['H13', 'H11', 'c'], ['H14', 'H12', 'c'], ['H12', 'H14', 'c'], ['H15', 'H31', 'c'], ['H31', 'H15', 'c'], ['H40', 'H15', 'c'], ['H15', 'H40', 'c'], ['H26', 'H7', 'c'], ['H16', 'H13', 'c'], ['H13', 'H16', 'c'], ['H16', 'H27', 'c'], ['H27', 'H16', 'c'], ['H19', 'H43', 'c'], ['H20', 'H41', 'c'], ['H21', 'H36', 'c'], ['H20', 'H35', 'c'], ['H33', 'H21', 'c'], ['H33', 'H30', 'c'], ['H43', 'H26', 'c'], ['H46', 'H25', 'c'], ['H45', 'H27', 'c'], ['H47', 'H31', 'c'], ['H17', 'H44', 'c'], ['H21', 'H33', 'c'], ['H35', 'H20', 'c'], ['H36', 'H21', 'c'], ['H41', 'H20', 'c'], ['H43', 'H19', 'c'], ['H30', 'H36', 'c'], ['H30', 'H33', 'c'], ['H36', 'H30', 'c'], ['H36', 'H32', 'c'], ['H33', 'H32', 'c'], ['H32', 'H33', 'c'], ['H32', 'H36', 'c'], ['H25', 'H46', 'c'], ['H26', 'H43', 'c'], ['H27', 'H45', 'c'], ['H31', 'H47', 'c'], ['H37', 'H48', 'c'], ['H48', 'H37', 'c'], ['H39', 'H49', 'c'], ['H49', 'H39', 'c'], ['H20', 'H3', 't'], ['H1', 'H26', 't'], ['H1', 'H19', 't'], ['H1', 'H7', 't'], ['H7', 'H19', 't'], ['H7', 'H26', 't'], ['H19', 'H26', 't'], ['H26', 'H19', 't'], ['H26', 'H7', 't'], ['H26', 'H1', 't'], ['H19', 'H7', 't'], ['H19', 'H1', 't'], ['H7', 'H1', 't'], ['H3', 'H20', 't'], ['H35', 'H3', 't'], ['H3', 'H35', 't'], ['H37', 'H3', 't'], ['H3', 'H37', 't'], ['H41', 'H3', 't'], ['H3', 'H41', 't'], ['H20', 'H37', 't'], ['H37', 'H20', 't'], ['H41', 'H20', 't'], ['H20', 'H41', 't'], ['H35', 'H37', 't'], ['H41', 'H35', 't'], ['H37', 'H35', 't'], ['H35', 'H20', 't'], ['H48', 'H20', 't'], ['H48', 'H3', 't'], ['H3', 'H48', 't'], ['H20', 'H48', 't'], ['H35', 'H48', 't'], ['H48', 'H35', 't'], ['H41', 'H37', 't'], ['H48', 'H37', 't'], ['H37', 'H41', 't'], ['H37', 'H48', 't'], ['H35', 'H41', 't'], ['H20', 'H35', 't'], ['H41', 'H48', 't'], ['H48', 'H41', 't'], ['H34', 'H1', 't'], ['H43', 'H1', 't'], ['H1', 'H43', 't'], ['H1', 'H34', 't'], ['H34', 'H7', 't'], ['H43', 'H7', 't'], ['H34', 'H19', 't'], ['H43', 'H19', 't'], ['H34', 'H26', 't'], ['H43', 'H26', 't'], ['H7', 'H43', 't'], ['H7', 'H34', 't'], ['H19', 'H43', 't'], ['H19', 'H34', 't'], ['H26', 'H43', 't'], ['H26', 'H34', 't'], ['H34', 'H43', 't'], ['H43', 'H34', 't'], ['H11', 'H4', 't'], ['H13', 'H4', 't'], ['H27', 'H4', 't'], ['H45', 'H4', 't'], ['H4', 'H45', 't'], ['H4', 'H27', 't'], ['H4', 'H13', 't'], ['H4', 'H11', 't'], ['H16', 'H45', 't'], ['H16', 'H4', 't'], ['H4', 'H16', 't'], ['H45', 'H16', 't'], ['H16', 'H27', 't'], ['H27', 'H16', 't'], ['H27', 'H45', 't'], ['H45', 'H27', 't'], ['H13', 'H16', 't'], ['H13', 'H45', 't'], ['H13', 'H27', 't'], ['H27', 'H13', 't'], ['H45', 'H13', 't'], ['H16', 'H13', 't'], ['H16', 'H11', 't'], ['H11', 'H16', 't'], ['H11', 'H27', 't'], ['H11', 'H13', 't'], ['H13', 'H11', 't'], ['H27', 'H11', 't'], ['H45', 'H11', 't'], ['H11', 'H45', 't'], ['H38', 'H6', 't'], ['H39', 'H6', 't'], ['H44', 'H6', 't'], ['H49', 'H6', 't'], ['H17', 'H6', 't'], ['H6', 'H38', 't'], ['H6', 'H39', 't'], ['H6', 'H44', 't'], ['H6', 'H49', 't'], ['H6', 'H17', 't'], ['H39', 'H38', 't'], ['H44', 'H38', 't'], ['H49', 'H38', 't'], ['H17', 'H38', 't'], ['H38', 'H39', 't'], ['H38', 'H44', 't'], ['H38', 'H49', 't'], ['H38', 'H17', 't'], ['H39', 'H44', 't'], ['H44', 'H39', 't'], ['H49', 'H39', 't'], ['H39', 'H17', 't'], ['H17', 'H39', 't'], ['H44', 'H17', 't'], ['H17', 'H44', 't'], ['H39', 'H49', 't'], ['H44', 'H49', 't'], ['H49', 'H44', 't'], ['H17', 'H49', 't'], ['H49', 'H17', 't'], ['H18', 'H5', 't'], ['H25', 'H5', 't'], ['H46', 'H5', 't'], ['H25', 'H18', 't'], ['H46', 'H18', 't'], ['H46', 'H25', 't'], ['H5', 'H18', 't'], ['H5', 'H25', 't'], ['H5', 'H46', 't'], ['H18', 'H46', 't'], ['H18', 'H25', 't'], ['H25', 'H46', 't'], ['H21', 'H2', 't'], ['H2', 'H21', 't'], ['H30', 'H21', 't'], ['H32', 'H21', 't'], ['H36', 'H21', 't'], ['H36', 'H32', 't'], ['H36', 'H30', 't'], ['H32', 'H36', 't'], ['H30', 'H36', 't'], ['H30', 'H32', 't'], ['H32', 'H30', 't'], ['H30', 'H2', 't'], ['H32', 'H2', 't'], ['H36', 'H2', 't'], ['H21', 'H32', 't'], ['H21', 'H30', 't'], ['H21', 'H36', 't'], ['H2', 'H36', 't'], ['H2', 'H32', 't'], ['H2', 'H30', 't'], ['H15', 'H31', 't'], ['H15', 'H29', 't'], ['H15', 'H28', 't'], ['H28', 'H15', 't'], ['H29', 'H15', 't'], ['H31', 'H15', 't'], ['H28', 'H31', 't'], ['H29', 'H31', 't'], ['H31', 'H29', 't'], ['H31', 'H28', 't'], ['H29', 'H28', 't'], ['H28', 'H29', 't'], ['H9', 'H29', 't'], ['H9', 'H28', 't'], ['H28', 'H9', 't'], ['H29', 'H9', 't'], ['H14', 'H12', 't'], ['H12', 'H14', 't'], ['H47', 'H15', 't'], ['H28', 'H47', 't'], ['H29', 'H47', 't'], ['H31', 'H47', 't'], ['H47', 'H31', 't'], ['H47', 'H29', 't'], ['H47', 'H28', 't'], ['H15', 'H47', 't'], ['H40', 'H15', 't'], ['H15', 'H40', 't'], ['H33', 'H36', 't'], ['H33', 'H32', 't'], ['H32', 'H33', 't'], ['H36', 'H33', 't'], ['H33', 'H30', 't'], ['H30', 'H33', 't'], ['H33', 'H21', 't'], ['H21', 'H33', 't'], ['H33', 'H2', 't'], ['H2', 'H33', 't'], ['H47', 'H40', 't'], ['H40', 'H47', 't'], ['H23', 'H15', 't'], ['H28', 'H23', 't'], ['H29', 'H23', 't'], ['H31', 'H23', 't'], ['H23', 'H28', 't'], ['H23', 'H29', 't'], ['H23', 'H31', 't'], ['H23', 'H47', 't'], ['H47', 'H23', 't'], ['H15', 'H23', 't'], ['H40', 'H23', 't'], ['H40', 'H31', 't'], ['H40', 'H29', 't'], ['H40', 'H28', 't'], ['H29', 'H40', 't'], ['H31', 'H40', 't'], ['H28', 'H40', 't']]
    Carbons = ['C39', 'C38', 'C35', 'C34', 'C37', 'C36', 'C31', 'C30', 'C33', 'C32', 'C8', 'C50', 'C9', 'C3', 'C2', 'C1', 'C5', 'C4', 'C22', 'C23', 'C20', 'C21', 'C26', 'C24', 'C25', 'C28', 'C7', 'C27', 'C6', 'C29', 'C18', 'C44', 'C52', 'C51', 'C45', 'C19', 'C13', 'C12', 'C11', 'C10', 'C17', 'C16', 'C15', 'C14', 'C46', 'C47', 'C40', 'C41', 'C42', 'C43', 'C49', 'C48']
    Hydrogens = ['H29', 'H28', 'H25', 'H24', 'H27', 'H26', 'H21', 'H20', 'H23', 'H22', 'H54', 'H55', 'H56', 'H57', 'H50', 'H51', 'H52', 'H53', 'H58', 'H59', 'H34', 'H35', 'H74', 'H75', 'H69', 'H68', 'H61', 'H60', 'H63', 'H62', 'H65', 'H64', 'H67', 'H66', 'H80', 'H32', 'H33', 'H30', 'H31', 'H36', 'H37', 'H78', 'H79', 'H76', 'H77', 'H38', 'H39', 'H72', 'H73', 'H70', 'H71', 'H18', 'H19', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H8', 'H9', 'H2', 'H3', 'H1', 'H6', 'H7', 'H4', 'H5', 'H47', 'H46', 'H45', 'H44', 'H43', 'H42', 'H41', 'H40', 'H49', 'H48']
    NewAtomData = {u'H29': [u'H', '29', u'2.6873055658786527', u'UNKNOWN', u'Adda5 10a', u'BrPurple'], u'H28': [u'H', '28', u'2.811533546084566', u'UNKNOWN', u'Adda5 10b', u'BrPurple'], u'H25': [u'H', '25', u'3.1481335664748524', u'UNKNOWN', u'xxx3 3', u'Red'], u'H24': [u'H', '24', u'3.2432720164801814', u'UNKNOWN', u'Adda5 9-OMe', 'none'], u'H27': [u'H', '27', u'3.0193099067656175', u'UNKNOWN', u'Adda5 2', u'green'], u'H26': [u'H', '26', u'3.1392030967710567', u'UNKNOWN', u'Arg4 4or5', u'blue'], u'H21': [u'H', '21', u'4.257933290801968', u'UNKNOWN', u'Glu6 2', u'black'], u'H20': [u'H', '20', u'4.284082233901146', u'UNKNOWN', u'Leu_a 2', u'pink'], u'H23': [u'H', '23', u'3.258307878268551', u'UNKNOWN', u'Adda5 9', u'BrPurple'], u'H22': [u'H', '22', u'3.3432', u'UNKNOWN', u'Mdha7 2-NMe', 'none'], u'C39': [u'C', '39', u'25.718352960295547', u'UNKNOWN', u'1', u'Leu_a 4'], u'C38': [u'C', '38', u'25.94191604186281', u'UNKNOWN', u'1', u'Leu_b 4'], u'C35': [u'C', '35', u'29.387795455565463', u'UNKNOWN', u'2', u'Arg4 3'], u'C34': [u'C', '34', u'33.05202631382084', u'UNKNOWN', u'2', u'Glu6 4'], u'C37': [u'C', '37', u'26.890676389793693', u'UNKNOWN', u'2', ''], u'C36': [u'C', '36', u'28.215570524928687', u'UNKNOWN', u'2', u'Glu6 3'], u'C31': [u'C', '31', u'38.803750201271924', u'UNKNOWN', u'1', u'Adda5 10'], u'C30': [u'C', '30', u'40.579336379268945', u'UNKNOWN', u'2', u'Leu_b 3'], u'C33': [u'C', '33', u'37.50453317921005', u'UNKNOWN', u'1', u'Adda5 8'], u'C32': [u'C', '32', u'38.34248778527212', u'UNKNOWN', u'1', u'Mdha7 2-NMe'], u'C8': [u'C', '8', u'158.73745055683938', u'UNKNOWN', u'0', ''], u'C50': [u'C', '50', u'NaN', u'UNKNOWN', u'-1', ''], u'C9': [u'C', '9', u'146.17091963301579', u'UNKNOWN', u'0', u'Mdha7 2'], u'H54': [u'H', '54', u'NaN', u'UNKNOWN', '', 'none'], u'H55': [u'H', '55', u'NaN', u'UNKNOWN', '', 'none'], u'H56': [u'H', '56', u'NaN', u'UNKNOWN', '', 'none'], u'H57': [u'H', '57', u'NaN', u'UNKNOWN', '', 'none'], u'H50': [u'H', '50', u'NaN', u'UNKNOWN', '', 'none'], u'H51': [u'H', '51', u'NaN', u'UNKNOWN', '', 'none'], u'H52': [u'H', '52', u'NaN', u'UNKNOWN', '', 'none'], u'H53': [u'H', '53', u'NaN', u'UNKNOWN', '', 'none'], u'C3': [u'C', '3', u'176.38408422929908', u'UNKNOWN', u'0', ''], u'C2': [u'C', '2', u'177.13929693039202', u'UNKNOWN', u'0', u'Adda5 1'], u'C1': [u'C', '1', u'179.17802794218707', u'UNKNOWN', u'0', u'xxx3 1'], u'H58': [u'H', '58', u'NaN', u'UNKNOWN', '', 'none'], u'H59': [u'H', '59', u'NaN', u'UNKNOWN', '', 'none'], u'C5': [u'C', '5', u'171.87404889939904', u'UNKNOWN', u'0', ''], u'C4': [u'C', '4', u'175.36434442909464', u'UNKNOWN', u'0', ''], u'C22': [u'C', '22', u'56.593076133092026', u'UNKNOWN', u'1', u'Adda5 3'], u'C23': [u'C', '23', u'55.32646829632585', u'UNKNOWN', u'1', u'Leu_a 2'], u'C20': [u'C', '20', u'58.56972768315379', u'UNKNOWN', u'1', u'Adda5 9-OMe'], u'C21': [u'C', '21', u'56.71602558995551', u'UNKNOWN', u'1', u'xxx3 2'], u'C26': [u'C', '26', u'52.97878113241867', u'UNKNOWN', u'1', u'Leu_b 2'], u'H34': [u'H', '34', u'2.018131300600909', u'UNKNOWN', u'Arg4 3b', u'blue (unkn. ppm)'], u'C24': [u'C', '24', u'54.63047254419408', u'UNKNOWN', u'1', u'Glu6 2'], u'C25': [u'C', '25', u'53.061885102822465', u'UNKNOWN', u'1', u'Arg4 2'], u'C28': [u'C', '28', u'42.022158828502626', u'UNKNOWN', u'0', u'xxx3 3'], u'H35': [u'H', '35', u'2.00325102523024', u'UNKNOWN', u'Leu_a 3b', u'pink'], u'H74': [u'H', '74', u'NaN', u'UNKNOWN', '', 'none'], u'H75': [u'H', '75', u'NaN', u'UNKNOWN', '', 'none'], u'C7': [u'C', '7', u'166.3985244254127', u'UNKNOWN', u'0', u'Mdha7 1'], u'C27': [u'C', '27', u'45.090015865483764', u'UNKNOWN', u'1', u'Adda5 2'], u'C6': [u'C', '6', u'170.37041201959872', u'UNKNOWN', u'0', ''], u'H69': [u'H', '69', u'NaN', u'UNKNOWN', '', 'none'], u'H68': [u'H', '68', u'NaN', u'UNKNOWN', '', 'none'], u'C29': [u'C', '29', u'40.794370545197715', u'UNKNOWN', u'1', u'Leu_a 3'], u'C18': [u'C', '18', u'114.57363089878591', u'UNKNOWN', u'2', u'Mdha7 3'], u'H61': [u'H', '61', u'NaN', u'UNKNOWN', '', 'none'], u'H60': [u'H', '60', u'NaN', u'UNKNOWN', '', 'none'], u'H63': [u'H', '63', u'NaN', u'UNKNOWN', '', 'none'], u'H62': [u'H', '62', u'NaN', u'UNKNOWN', '', 'none'], u'H65': [u'H', '65', u'NaN', u'UNKNOWN', '', 'none'], u'H64': [u'H', '64', u'NaN', u'UNKNOWN', '', 'none'], u'H67': [u'H', '67', u'NaN', u'UNKNOWN', '', 'none'], u'H66': [u'H', '66', u'NaN', u'UNKNOWN', '', 'none'], u'C44': [u'C', '44', u'16.355959882491486', u'UNKNOWN', u'1', u'Adda5 8-Me'], u'C52': [u'C', '52', u'NaN', u'UNKNOWN', u'-1', ''], u'C51': [u'C', '51', u'NaN', u'UNKNOWN', u'-1', ''], u'C45': [u'C', '45', u'15.830987431073462', u'UNKNOWN', u'1', u'Adda5 2-Me'], u'C19': [u'C', '19', u'88.18922646066797', u'UNKNOWN', u'1', u'Adda5 9'], u'H80': [u'H', '80', u'NaN', u'UNKNOWN', '', 'none'], u'C13': [u'C', '13', u'133.89420552190214', u'UNKNOWN', u'0', u'Adda5 6'], u'C12': [u'C', '12', u'137.05569093529456', u'UNKNOWN', u'1', u'Adda5 7'], u'C11': [u'C', '11', u'138.9259710321553', u'UNKNOWN', u'1', u'Adda5 5'], u'C10': [u'C', '10', u'140.45302092384435', u'UNKNOWN', u'0', u'Adda5 11'], u'C17': [u'C', '17', u'126.36855882738689', u'UNKNOWN', u'1', u'Adda5 4'], u'C16': [u'C', '16', u'126.943', u'UNKNOWN', u'1', u'Adda5 14'], u'C15': [u'C', '15', u'129.0953465463974', u'UNKNOWN', u'1', u'Adda5 13/15'], u'C14': [u'C', '14', u'130.4069434059111', u'UNKNOWN', u'1', u'Adda5 12/16'], u'H32': [u'H', '32', u'2.5509392493442515', u'UNKNOWN', u'Glu6 4a', u'Black'], u'H33': [u'H', '33', u'2.128', u'UNKNOWN', u'Glu6 3b', u'Black'], u'H30': [u'H', '30', u'2.659298952306115', u'UNKNOWN', u'Glu6 4b', u'Black'], u'H31': [u'H', '31', u'2.5921992783619596', u'UNKNOWN', u'Adda5 8', u'BrPurple'], u'H36': [u'H', '36', u'1.9402716497687358', u'UNKNOWN', u'Glu6 3a', u'Black'], u'H37': [u'H', '37', u'1.7851696824186187', u'UNKNOWN', u'Leu_a 4', u'pink'], u'H78': [u'H', '78', u'NaN', u'UNKNOWN', '', 'none'], u'H79': [u'H', '79', u'NaN', u'UNKNOWN', '', 'none'], u'H76': [u'H', '76', u'NaN', u'UNKNOWN', '', 'none'], u'H77': [u'H', '77', u'NaN', u'UNKNOWN', '', 'none'], u'H38': [u'H', '38', u'1.7836990104616657', u'UNKNOWN', u'Leu_b 3b', u'ThinPurple'], u'H39': [u'H', '39', u'1.616084103489747', u'UNKNOWN', u'Leu_b 4', u'ThinPurple'], u'H72': [u'H', '72', u'NaN', u'UNKNOWN', '', 'none'], u'H73': [u'H', '73', u'NaN', u'UNKNOWN', '', 'none'], u'H70': [u'H', '70', u'NaN', u'UNKNOWN', '', 'none'], u'H71': [u'H', '71', u'NaN', u'UNKNOWN', '', 'none'], u'H18': [u'H', '18', u'4.503443610797938', u'UNKNOWN', u'xxx3 1', u'Red'], u'H19': [u'H', '19', u'4.3102623232927515', u'UNKNOWN', u'Arg4 2', u'blue'], u'C46': [u'C', '46', u'15.353739747966165', u'UNKNOWN', u'1', u'xxx3 3-Me'], u'C47': [u'C', '47', u'12.746720331531092', u'UNKNOWN', u'1', u'Adda5 6-Me'], u'C40': [u'C', '40', u'23.7593101718234', u'UNKNOWN', u'0', u'Leu_a 5b'], u'C41': [u'C', '41', u'23.483520152417444', u'UNKNOWN', u'1', u'Leu_a 5a'], u'C42': [u'C', '42', u'21.153094488437088', u'UNKNOWN', u'0', u'Leu_b 5b'], u'C43': [u'C', '43', u'20.969639448250042', u'UNKNOWN', u'1', u'Leu_b 5a'], u'H10': [u'H', '10', u'7.163150831849728', u'UNKNOWN', u'Adda5 14', 'none'], u'H11': [u'H', '11', u'6.241529648164774', u'UNKNOWN', u'Adda5 5', u'green'], u'H12': [u'H', '12', u'5.90658478753204', u'UNKNOWN', u'Mdha7 3b', u'Mdha'], u'H13': [u'H', '13', u'5.470184147427857', u'UNKNOWN', u'Adda5 4', u'green'], u'H14': [u'H', '14', u'5.446686101467496', u'UNKNOWN', u'Mdha7 3a', u'Mdha'], u'H15': [u'H', '15', u'5.42440228307506', u'UNKNOWN', u'Adda5 7', u'BrPurple'], u'H16': [u'H', '16', u'4.587264376697401', u'UNKNOWN', u'Adda5 3', u'green'], u'H17': [u'H', '17', u'4.5340029160882676', u'UNKNOWN', u'Leu_b 2', u'ThinPurple'], u'C49': [u'C', '49', u'NaN', u'UNKNOWN', u'-1', ''], u'C48': [u'C', '48', u'NaN', u'UNKNOWN', u'-1', ''], u'H8': [u'H', '8', u'7.2427483244499715', u'UNKNOWN', u'Adda5 13/15', 'none'], u'H9': [u'H', '9', u'7.1818316649497635', u'UNKNOWN', u'Adda5 12/16', u'BrPurple'], u'H2': [u'H', '2', u'8.456445498313027', u'UNKNOWN', u'Glu6 2-NH', u'Black'], u'H3': [u'H', '3', u'8.24641901177914', u'UNKNOWN', u'Leu_a 2-NH', u'pink'], u'H1': [u'H', '1', u'8.679104567926453', u'UNKNOWN', u'Arg4 2-NH', u'blue'], u'H6': [u'H', '6', u'7.719841896667642', u'UNKNOWN', u'Leu_b 2-NH', u'ThinPurple'], u'H7': [u'H', '7', u'7.365164441665352', u'UNKNOWN', u'Arg4 5-NH', u'blue'], u'H4': [u'H', '4', u'7.849355744697838', u'UNKNOWN', u'Adda5 3-NH', u'green'], u'H5': [u'H', '5', u'7.758299787555936', u'UNKNOWN', u'xxx3 2-NH', u'Red'], u'H47': [u'H', '47', u'1.0037158759114673', u'UNKNOWN', u'Adda5 8-Me', u'BrPurple'], u'H46': [u'H', '46', u'1.0426935176248742', u'UNKNOWN', u'xxx3 3-Me', u'Red'], u'H45': [u'H', '45', u'1.0477474199026915', u'UNKNOWN', u'Adda5 2-Me', u'green'], u'H44': [u'H', '44', u'1.512788639009154', u'UNKNOWN', u'Leu_b 3a', u'ThinPurple'], u'H43': [u'H', '43', u'1.523446369904363', u'UNKNOWN', u'Arg4 3a', u'blue (unkn. ppm)'], u'H42': [u'H', '42', u'1.5263932834276566', u'UNKNOWN', '', u'Unknown'], u'H41': [u'H', '41', u'1.5950342329216327', u'UNKNOWN', u'Leu_a 3a', u'pink'], u'H40': [u'H', '40', u'1.610471260625012', u'UNKNOWN', u'Adda5 6-Me', u'BrPurple'], u'H49': [u'H', '49', u'0.8817489731198487', u'UNKNOWN', u'Leu_b 5', u'ThinPurple'], u'H48': [u'H', '48', u'0.887982167867667', u'UNKNOWN', u'Leu_a 5', u'pink']}
    #printData(Carbons, Hydrogens, correlations)
    #printForCarbons(Carbons, Hydrogens, correlations, NewAtomData)
    print 
    #printAllHydrogens(Carbons, Hydrogens, correlations, NewAtomData)
    #printAtomNames(Carbons, Hydrogens, NewAtomData)
    print
    #printInTableFormat(Carbons, Hydrogens, NewAtomData, correlations, getPrintTableFormat())
    exportSciTable(Carbons, Hydrogens, NewAtomData, correlations)
    #for c in Carbons:
    #    print c, NewAtomData[c]

    











