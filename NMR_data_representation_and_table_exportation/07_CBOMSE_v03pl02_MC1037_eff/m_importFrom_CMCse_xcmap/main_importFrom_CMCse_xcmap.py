from m.mfi import imp
exec(imp())

def main_importFrom_CMCse_xcmap(copy_xcmap_from_external_path, cmc_project_path,  file_and_project_name):
    #print 'main_importFrom_CMCse_xcmap.py'

    #CMCseFilename = 'strucelu_MC1037_DMSO'
    CMCseFilename = file_and_project_name
    
    tmp = CMCseFilename
    """
    i_fsf('oldMethods.copyCMCseFile')
    copyCMCseFile(CMCseFilename)
    #"""
    #i('copyCMCseFileFromExplicitPlace')
    if copy_xcmap_from_external_path:
        i_fsf('m_importFrom_CMCse_xcmap.copyCMCseFileFromExplicitPlace')
        copyCMCseFileFromExplicitPlace(cmc_project_path,  file_and_project_name)
    
    CMCseFilename = tmp
    #CMCseFilename = tmp+'.xcmap'



    
    #i('fun_readCMCse_XML')
    i_fsf('m_importFrom_CMCse_xcmap.fun_readCMCse_XML')

    inName = CMCseFilename
    NewAtomData, corList, HList, CList, OldAtomDataFormat = fun_readCMCse_XML(inName)
    
    #global atomData
    atomData = OldAtomDataFormat
    Hydrogens = HList
    Carbons = CList
    correlations = corList

    return [atomData, Hydrogens, Carbons, correlations, NewAtomData,]
