#import win32api


def copyCMCseFileFromExplicitPlace(cmc_project_path,  file_and_project_path):
    srcBase = cmc_project_path
    CMCseFilename = file_and_project_path
    import os
    import shutil
    #srcBase = 'S:/fileFolder_128GB/Thesis_collected/CMCse_projects_sync_root/shortpath_MC1037/SelectionOf_AW_wash_MC1037/instrument/data/jajaabae/nmr/20160701_Restart_Selec_AW_wash_MC1037'
    
    src = srcBase+'/'+CMCseFilename+'/'+CMCseFilename+'.xcmap'
    dst = os.getcwd()+'/'+CMCseFilename
    print src
    print dst
    shutil.copyfile(src, dst)



def old_copyCMCseFileFromExplicitPlace(CMCseFilename):
    import os
    import shutil
    #CMCseFilenameMain=CMCseFilename.split('.')[0]
    #root, home = os.getcwd().split('ContinousBackup')
    #src = 'M:/Desktop/Studier/NMR_DATA_manuallySelected_of_copiedFromR/AW_wash_MC1037/data/SelectionOf_AW_wash_MC1037/nmr/CMCseFormat__SelectionOf_AW_wash_MC1037/'+CMCseFilenameMain+'/'+CMCseFilename

    #srcBase = 'C:/Users/jajaabae/Google Drive/ContinousBackup/Thesis/MC1037/SelectionOf_AW_wash_MC1037/instrument/data/jajaabae/nmr/20160701_Restart_Selec_AW_wash_MC1037'
    srcBase = 'S:/fileFolder_128GB/google_drive/ContinousBackup/Thesis/MC1037/SelectionOf_AW_wash_MC1037/instrument/data/jajaabae/nmr/20160701_Restart_Selec_AW_wash_MC1037'
    #srcBase = 'S:/fileFolder_128GB/Thesis_collected/CMCse_projects_sync_root/CMCse_projects_sync_root/Users/jajaabae/Google Drive/ContinousBackup/Thesis/MC1037/SelectionOf_AW_wash_MC1037/instrument/data/jajaabae/nmr/20160701_Restart_Selec_AW_wash_MC1037'
    srcBase = 'S:/fileFolder_128GB/Thesis_collected/CMCse_projects_sync_root/shortpath_MC1037/SelectionOf_AW_wash_MC1037/instrument/data/jajaabae/nmr/20160701_Restart_Selec_AW_wash_MC1037'
    
    src = srcBase+'/'+CMCseFilename+'/'+CMCseFilename+'.xcmap'
    dst = os.getcwd()+'/'+CMCseFilename
    print src
    print dst
    shutil.copyfile(src, dst)

    
    #shutil.copyfile("\\\\?\\"+src, dst) #Failed
    #src = win32api.GetShortPathName(src)
    #shutil.copyfile(src, dst)

    #print root, home

