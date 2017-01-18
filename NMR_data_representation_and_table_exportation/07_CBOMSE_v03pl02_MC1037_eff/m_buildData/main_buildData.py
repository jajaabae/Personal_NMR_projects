from m.mfi import imp
exec(imp())

def main_buildData(buildContainer):
    
    HPrefix = buildContainer.HPrefix
    CPrefix = buildContainer.CPrefix
    Hydrogens = buildContainer.Hydrogens
    Carbons = buildContainer.Carbons
    correlations = buildContainer.correlations
    Bonds = buildContainer.Bonds
    prelimBonds = buildContainer.prelimBonds
    

    i_fsf('m_buildData.renameAtoms')
    i_fsf('m_buildData.makeHSQCBonds')
    i_fsf('m_buildData.CCFromCOSY')
    i_fsf('m_buildData.bondsClean')
    i_fsf('m_buildData.getOtherFromCor')
    i_fsf('m_buildData.addBondForSingleHWithCOSY')
    i_fsf('m_buildData.assignGroup')
    i_fsf('m_buildData.makeGroups')
    i_fsf('m_buildData.getNonCorrelatedAtoms')


    correlations = renameAtoms(HPrefix, CPrefix, Hydrogens, Carbons, correlations)

    #print correlations
    
    makeHSQCBonds(correlations, Bonds)

    ###print correlations

    def makePrelimBonds(correlations, Bonds, Carbons, prelimBonds):
        CCFromCOSY(correlations, Bonds, Carbons, prelimBonds)
    makePrelimBonds(correlations, Bonds, Carbons, prelimBonds)

    #print 'Bonds:', Bonds #=> 'q'

    Bonds = bondsClean(Bonds)
    prelimBonds = bondsClean(prelimBonds)

    #####print correlations

    ##COSY: if no C or have same C: add cosy-bond.
    addBondForSingleHWithCOSY(correlations, getOtherFromCor, Bonds)
    Bonds = bondsClean(Bonds)
    #print 'Bonds:', Bonds #=> 'q'

    #Groups of atoms
    groups = makeGroups(prelimBonds, Bonds, Hydrogens, Carbons, assignGroup)

    # redundant atoms
    atoms = Hydrogens+Carbons
    allConnections = correlations+Bonds+prelimBonds #Warning: This includes tocsy which is not handeled!!!
    redundantAtoms = getNonCorrelatedAtoms(atoms, allConnections)
    
    correlations = bondsClean(correlations)

    #print correlations
    #print '***********************************************************'
    #print 'Bonds:', Bonds #=> 'q'

    return [correlations, Bonds, prelimBonds, Bonds, groups, atoms, allConnections, redundantAtoms]


