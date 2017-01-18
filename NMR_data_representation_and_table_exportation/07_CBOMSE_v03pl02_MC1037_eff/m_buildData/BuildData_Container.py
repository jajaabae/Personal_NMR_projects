from m.mfi import imp
exec(imp())

class BuildData_Container():

    def fillContainer(  self,
                        HPrefix,
                        CPrefix,
                        Hydrogens,
                        Carbons,
                        correlations,
                        Bonds,
                        prelimBonds,
                      ):
        
        BuildData_Container.HPrefix = HPrefix
        BuildData_Container.CPrefix = CPrefix
        BuildData_Container.Hydrogens = Hydrogens
        BuildData_Container.Carbons = Carbons
        BuildData_Container.correlations = correlations
        BuildData_Container.Bonds = Bonds
        BuildData_Container.prelimBonds = prelimBonds

