from m.mfi import imp
exec(imp())

def reduceListToContent(listOfItemsOrTuples, atomsInMal):
    #print atomsInMal
    redList = []
    for e in listOfItemsOrTuples:
        In_atomsInMal = False
        if type(e)==type(''):
            In_atomsInMal = e in atomsInMal
        elif type(e)==type([]):
            In_atomsInMal = e[0] in atomsInMal and e[1] in atomsInMal
        else:
            pass
        if In_atomsInMal:
            redList += [e]
    return redList
    


    
    
def getAtomsInMal(NewAtomData, coordDict):
    atomsInMal = []

    rni('NewAtomDataContainer')
    NADC = NewAtomDataContainer(NewAtomData)
    #print NADC.numHasPartner('CMe-Asp3 3-Me')
    #print NADC.strHasPartner('C31')
    
    for e in coordDict:
        #NADC.getNumNameFromStrName(e)
        #print e, NADC.getNumNameFromStrName(e)
        if not NADC.getNumNameFromStrName(e) == None:
            atomsInMal += [NADC.getNumNameFromStrName(e)]
    
    return atomsInMal

import copy
def reduceDataToContentOfMal(buildt_data_cnt_COPY, NewAtomData, coordDict):
    
    print '************'
    atomsInMal = getAtomsInMal(NewAtomData, coordDict)



    i_fsf('m_exportToChemdraw.Container_for_BuildtData')
    buildt_data_cnt_edit = Container_for_BuildtData()
    
    HPrefix = buildt_data_cnt_COPY.HPrefix
    Hydrogens = reduceListToContent(buildt_data_cnt_COPY.Hydrogens, atomsInMal)
    Carbons = reduceListToContent(buildt_data_cnt_COPY.Carbons, atomsInMal)
    Bonds = reduceListToContent(buildt_data_cnt_COPY.Bonds, atomsInMal)
    prelimBonds = reduceListToContent(buildt_data_cnt_COPY.prelimBonds, atomsInMal)
    correlations = reduceListToContent(buildt_data_cnt_COPY.correlations, atomsInMal)
    redundantAtoms = reduceListToContent(buildt_data_cnt_COPY.redundantAtoms, atomsInMal)

    buildt_data_cnt_edit.fillContainer(  
                            HPrefix,
                            Hydrogens,
                            Carbons,
                            Bonds,
                            prelimBonds,
                            correlations,
                            redundantAtoms,)
    
    print '************'
    #return buildt_data_cnt_COPY
    return buildt_data_cnt_edit


def main_exportToChemdraw(cnt, buildt_data_cnt,
                            ):

    #### COLORS ####
    """
    color="0", Black
    color="4", Red
    color="5", Yellow
    color="6", Green
    color="7", Cyan
    color="8", Blue
    color="9", Magenta
    #"""

    import m_exportToChemdraw.writeCDXML
    reload(m_exportToChemdraw.writeCDXML)
    i_fsf('m_exportToChemdraw.writeCDXML')


    import m_exportToChemdraw.CD_ExportSettingsContainer
    reload(m_exportToChemdraw.CD_ExportSettingsContainer)
    i_fsf('m_exportToChemdraw.CD_ExportSettingsContainer')

    #"""
    onlyFromMal = False
    nameAdd = ''
    inName = 'MC_mal.cdxml'
    i_fsf('m_cdxml_mal.fun_extract_coordinates')
    coordDict = fun_extract_coordinates(inName)# get coordinates from 'MC_mal.cdxml'

    #buildt_data_cnt_COPY = buildt_data_cnt
    buildt_data_cnt_COPY = copy.deepcopy(buildt_data_cnt)
    if onlyFromMal:
        buildt_data_cnt_COPY = reduceDataToContentOfMal(buildt_data_cnt_COPY, cnt.NewAtomData, coordDict)
    
    corExpList = [
        't',
        'cmr',
        'tm',
        'mr',
        '',
        'c',
        'm',
        'r',
        'ctmr',
        ]
    for cor in corExpList:
        correlations = cor
        #bonds = ['CH', 'HH', 'CC']
        bonds = ['CH',]
        settingsContainer = CD_ExportSettingsContainer(
            bonds = bonds,
            correlations = correlations,
            )
        name='out_test_'+nameAdd+cor
        writeCDXML(cnt, buildt_data_cnt_COPY, settingsContainer,
                   name, coordDict,
                   )
    #"""






"""
    onlyFromMal = True
    inName = 'MC_mal_Leu2.cdxml'
    nameAdd = 'Leu2_'
    i_fsf('m_cdxml_mal.fun_extract_coordinates')
    coordDict = fun_extract_coordinates(inName)# get coordinates from 'MC_mal.cdxml'

    #buildt_data_cnt_COPY = buildt_data_cnt
    buildt_data_cnt_COPY = copy.deepcopy(buildt_data_cnt)
    if onlyFromMal:
        buildt_data_cnt_COPY = reduceDataToContentOfMal(buildt_data_cnt_COPY, cnt.NewAtomData, coordDict)
    
    corExpList = [
        #'t',
        #'cmr',
        #'tm',
        #'mr',
        #'',
        'c',
        #'m',
        #'r',
        #'ctmr',
        ]
    for cor in corExpList:
        correlations = cor
        #bonds = ['CH', 'HH', 'CC']
        bonds = []
        settingsContainer = CD_ExportSettingsContainer(
            bonds = bonds,
            correlations = correlations,
            )
        name='out_test_'+nameAdd+cor
        writeCDXML(cnt, buildt_data_cnt_COPY, settingsContainer,
                   name, coordDict,
                   )
"""



