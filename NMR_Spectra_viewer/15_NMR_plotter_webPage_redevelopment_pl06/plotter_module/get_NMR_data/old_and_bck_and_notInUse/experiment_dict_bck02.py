import os
from m.settings_module import get_settings_from_file

class Content_of_data():
    """
    needs:
    - list/dict of spectra
    - ...
    """
    NotImplemented
    
def get_dict_of_spectra_type_with_paths():
    """
    spectra_path_dict = {'ROESY':'Bruker_NMR_spectra/23/pdata/1',
                          'TOCSY':'Bruker_NMR_spectra/11/pdata/1',
                          'COSY':'Bruker_NMR_spectra/20/pdata/1',
                          'NOESY':'Bruker_NMR_spectra/21/pdata/1',
                          'HSQC':'Bruker_NMR_spectra/15/pdata/1',
                          'HMBC':'Bruker_NMR_spectra/16/pdata/1',
                          } #tmp
    #"""
    
    settings_dict = get_settings_from_file()
    spec_dir = settings_dict['spectra_dir']

    spectra_list_file_name = 'list_of_spectra.txt'
    spectra_list_file_in_path = os.path.join(spec_dir, spectra_list_file_name)
    f = open(spectra_list_file_in_path,'r')
    a_list = f.readlines()
    f.close()

    spectra_path_dict = {}
    for e in a_list:
        e = e.replace('\n','').split('\t')
        spec_type = e[0]
        spectrum = e[1]
        spectrum_in_path = os.path.join(spec_dir, spectrum)

        spectra_path_dict[spec_type] = spectrum_in_path
    
    return spectra_path_dict


"""
def test():
    #from m.settings_module import get_settings_from_file
    settings_dict = get_settings_from_file()
    spec_dir = settings_dict['spectra_dir']

    spectra_list_file_name = 'list_of_spectra.txt'

    #print spec_dir
    #print spectra_list_file_name

    
    spectra_list_file_in_path = os.path.join(spec_dir, spectra_list_file_name)
    f = open(spectra_list_file_in_path,'r')
    a_list = f.readlines()
    f.close()

    spectra_path_dict = {}
    for e in a_list:
        e = e.replace('\n','').split('\t')
        spec_type = e[0]
        spectrum = e[1]
        spectrum_in_path = os.path.join(spec_dir, spectrum)

        spectra_path_dict[spec_type] = spectrum_in_path
    
    print spectra_path_dict
#"""
    
if __name__ == '__main__':
    #test()
    print get_dict_of_spectra_type_with_paths()
