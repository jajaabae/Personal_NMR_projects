from m.mfi import imp
exec(imp())

def writeCDXML(cnt, buildt_data_cnt, settingsContainer,
               name,
               coordDict,
               ):

    
    Hydrogens = buildt_data_cnt.Hydrogens
    Carbons = buildt_data_cnt.Carbons
    Bonds = buildt_data_cnt.Bonds
    prelimBonds = buildt_data_cnt.prelimBonds
    correlations = buildt_data_cnt.correlations
    redundantAtoms = buildt_data_cnt.redundantAtoms
    

    explanatoryBondColor = settingsContainer.keywords['explanatoryBondColor']
    writeCorrelations = settingsContainer.keywords['writeCorrelations']
    
    
    i_fsf('m_exportToChemdraw.textForBond')
    i_fsf('m_exportToChemdraw.getTextStart')
    i_fsf('m_exportToChemdraw.getTextEnd')
    i_fsf('m_exportToChemdraw.textForCorrelation')
    i_fsf('m_exportToChemdraw.bondTextH')
    i_fsf('m_exportToChemdraw.bondTextC')
    
    out = open(name+'.cdxml', 'w')
    out.write(getTextStart())

    for H in Hydrogens:
        if H not in redundantAtoms:
            out.write(bondTextH(H, cnt, coordDict))
    for C in Carbons:
        if C not in redundantAtoms:
            out.write(bondTextC(C, cnt, coordDict))


#"""
    ###cosy and hsqc ###
    for B in Bonds: 
        color = 3
        #print B
        if len(B)>2 and 'HH' in settingsContainer.keywords['bonds']:
            if B[2]=='c':
                color = 7
                out.write(textForBond(B, color, cnt))
        if len(B)>2 and 'CH' in settingsContainer.keywords['bonds']:
            if B[2]=='q':
                if explanatoryBondColor:
                    color = 9
                    out.write(textForBond(B, color, cnt))
        #out.write(textForBond(B, color, cnt))
#"""


    ### C-C bonds ###
    for B in prelimBonds:
        if 'CC' in settingsContainer.keywords['bonds']:
            color = settingsContainer.getBondColor('CC')
            #print color
            #color = 3
            #if explanatoryBondColor:
            #    color = 8
            #print textForBond(B, color)
            out.write(textForBond(B, color, cnt))





    ### sort correlations to get COSY last and on-top ###    
    def getKey(item):
        return item[2]
    correlations = sorted(correlations, key=getKey, reverse=True)
    #print correlations

    ### correlations ###
    if writeCorrelations:
        for cor in correlations:
            #print cor
            #print settingsContainer.keywords['correlations']
            if cor[2] in settingsContainer.keywords['correlations']:
                cor_color = settingsContainer.getCorColor(cor[2])
                out.write(textForCorrelation(cor, cor_color, cnt))
                #print settingsContainer.keywords['correlations'], cor
                #print type(correlations)



                    
    out.write(getTextEnd())
    out.close()
    print 'Exported:', name



