import time
start_time_main = time.time()

# make compitable with Android (qPython)
import os 
p = os.path.realpath(__file__).replace('\\', '/').split('/')
p = '/'.join(p[0:-1])
os.chdir(p)

import random
import math

from m.mfi import imp
exec(imp())
#i('aFun') # Import (from 'm')
#rni('aFun') #Reload aNd Import (to test the function) (from 'm')
#iaff('m') #Import All From Folder
#i_fsf('sof.someOtherFunction') #Import From Spesific Folder


### settings ###
copy_xcmap_from_external_path = True
#copy_xcmap_from_external_path = False
CMCseXML=True
#---------------


### other definitions ###
ok='ok'

HPrefix='H'
HPrefixNum='111'
CPrefix='C'
CPrefixNum='222'


Hydrogens = []
Carbons = []
correlations = []
Bonds = []
prelimBonds = []
groups = []
#------------------------


###########################################################################
# Import data
if CMCseXML:
    i_fsf('m_importFrom_CMCse_xcmap.main_importFrom_CMCse_xcmap')
    cmc_project_path = r'S:\fileFolder_128GB\Thesis_collected\NMR_DATA\MC1037_eff\forTesting_SelectionOf_AW_wash_MC1037_onS\instrument\data\jajaabae\nmr\20160701_Restart_Selec_AW_wash_MC1037'
    file_and_project_path = "strucelu_for_testing"
    [atomData, Hydrogens, Carbons, correlations, NewAtomData] = main_importFrom_CMCse_xcmap(copy_xcmap_from_external_path, cmc_project_path,  file_and_project_path)

print 'atomData', atomData
print
print 'Hydrogens', Hydrogens
print
print 'Carbons', Carbons
print
print 'correlations', correlations
print
print 'NewAtomData', NewAtomData
print


###########################################################################
print '###################'
###########################################################################



i_fsf('m_buildData.BuildData_Container')
buildContainer = BuildData_Container()
buildContainer.fillContainer(
                        HPrefix,
                        CPrefix,
                        Hydrogens,
                        Carbons,
                        correlations,
                        Bonds,
                        prelimBonds,
                        )
i_fsf('m_buildData.main_buildData')
[correlations, Bonds, prelimBonds, Bonds, groups, atoms, allConnections, redundantAtoms] = main_buildData(buildContainer)


############################################################################
def getppmText(NameOfAtom, decimals):
    global atomData
    ppmText = '()'
    if NameOfAtom in atomData:
        #print atomData[NameOfAtom]
        ppmText = "({0:.{1}f})".format(float(atomData[NameOfAtom]), decimals)
    return ppmText


############################################################################
# exportToChemdraw: CDXML

i_fsf('m_exportToChemdraw.Container_for_BuildtData')
buildt_data_cnt = Container_for_BuildtData()
buildt_data_cnt.fillContainer(  
                            HPrefix,
                            Hydrogens,
                            Carbons,
                            Bonds,
                            prelimBonds,
                            correlations,
                            redundantAtoms,)

i_fsf('m_exportToChemdraw.makeGridWithCDPageValues')
grid = makeGridWithCDPageValues(groups)

rni('Container')
cnt = Container()
cnt.fillContainer(HPrefix,
                      HPrefixNum,
                      CPrefix,
                      CPrefixNum,
                      getppmText,
                      groups,
                      grid,
                      #coordDict,
                      NewAtomData)

import m_exportToChemdraw.main_exportToChemdraw
reload(m_exportToChemdraw.main_exportToChemdraw)
i_fsf('m_exportToChemdraw.main_exportToChemdraw')
main_exportToChemdraw(cnt, buildt_data_cnt)






############################################################################
if False:
#if True:
    i('fun_WriteMatrixFromCorrelations')
    fun_WriteMatrixFromCorrelations(Hydrogens, Carbons, correlations, atomData)



############################################################################
#"""
from m_manual_data.import_manual_data_table import import_manual_data_table, print_imported_manual_data
the_file = open("manual_data_table.csv", 'r')
md_object = import_manual_data_table(the_file)
the_file.close()
#print_imported_manual_data(md_object)
#"""

############################################################################
if False:
#if True:
    print
    import m_exportSciTables.fun_exportSciTables
    reload(m_exportSciTables.fun_exportSciTables)
    i_fsf('m_exportSciTables.fun_exportSciTables')
    convertKvownNames = True
    #convertKvownNames = False
    convertKvownNamesToNumbers = True
    onlyPureRoesyCorrelations=True
    #onlyPureRoesyCorrelations=False
    fun_exportSciTables(Carbons, Hydrogens, NewAtomData, correlations, convertKvownNames, convertKvownNamesToNumbers, onlyPureRoesyCorrelations, md_object)
    print 


############################################################################
#if False:
if True:
    print
    import m_exportSciTables.fun_exportSciTables_v02
    reload(m_exportSciTables.fun_exportSciTables_v02)
    i_fsf('m_exportSciTables.fun_exportSciTables_v02')
    convertKvownNames = True
    #convertKvownNames = False
    convertKvownNamesToNumbers = True
    onlyPureRoesyCorrelations=True
    #onlyPureRoesyCorrelations=False
    fun_exportSciTables_v02(Carbons, Hydrogens, NewAtomData, correlations, convertKvownNames, convertKvownNamesToNumbers, onlyPureRoesyCorrelations, md_object)
    print

    
############################################################################
#extra outputs:

#print Hydrogens

############################################################################
elapsed_time = time.time() - start_time_main
print 'elapsed time: '
print elapsed_time
time.sleep(5)











