import nmrglue as ng

def read_Bruker_2D(src):
    """Done"""
    #src = 'Bruker_NMR_spectra/23/pdata/1'
    attr_dic, spectrum_array = ng.bruker.read_pdata(src)
    return attr_dic, spectrum_array
