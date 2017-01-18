class Container_for_BuildtData():
    HPrefix = None
    Hydrogens = None
    Carbons = None
    Bonds = None
    prelimBonds = None
    correlations = None
    redundantAtoms = None



    
    def fillContainer(self,
                        HPrefix,
                        Hydrogens,
                        Carbons,
                        Bonds,
                        prelimBonds,
                        correlations,
                        redundantAtoms,
                        ):
        Container_for_BuildtData.HPrefix = HPrefix
        Container_for_BuildtData.Hydrogens = Hydrogens
        Container_for_BuildtData.Carbons = Carbons
        Container_for_BuildtData.Bonds = Bonds
        Container_for_BuildtData.prelimBonds = prelimBonds
        Container_for_BuildtData.correlations = correlations
        Container_for_BuildtData.redundantAtoms = redundantAtoms

        
        

