from plotter_module.get_NMR_data.experiment_dict import get_dict_of_spectra_type_with_paths
from plotter_module.get_NMR_data.read_Bruker_2D import read_Bruker_2D
import numpy as np

def test_extracting_attr_from_dic(attr_dic):
    #print attr_dic
    
    #for e in attr_dic['procs']:
    #    print e, attr_dic['procs'][e]
    #    #print e, attr_dic['proc2s'][e]

    dF2 = attr_dic['procs']
    dF1 = attr_dic['proc2s']

    interesting_elements=[
        'AXNAME',
        'AXNUC',
        'FT_mod',
        'FTSIZE',
        'OFFSET',
        'PHC0',
        'PHC1',
        'SF',
        'SI',
        'SINO',
        'SIOLD',
        'SREGLST',
        'STSI',
        'SW_p',
        'TDeff',
        'WDW',
        'XDIM',
        'YMAX_p',
        'YMIN_p',
        ]
    for e in interesting_elements:
        print e, dF2[e]

    print '**'
    
    #print 'F2_SW*', dF2['SW_p'] / dF2['SF']
    #print 'F1_SW*', dF1['SW_p'] / dF1['SF']

    for d in [dF2]:
        print d['AXNAME'], d['AXNUC']
        SW = d['SW_p'] / d['SF']
        print 'SW*', SW
        OFFSET = d['OFFSET']
        print 'OFFSET', OFFSET, '(ca x_neg)'
        zero_ppm = OFFSET-SW
        print 'zero_ppm*', zero_ppm, '(ca x_pos)'
        #print np.linspace(5,-2,10)
        SI = d['SI']
        print 'SI', SI
        axis = np.linspace(OFFSET,zero_ppm,SI)
        print axis.shape


def reconstruct_dict(attr_dic, F_dims):
    """
    replaces proc2s and procs with F1 and F2
    """
    reconstructed_dict = {}
    for axis_from_dict in attr_dic:
        #print e
        for F_dim in F_dims:
            #print attr_dic[e]['AXNAME'] == w
            if attr_dic[axis_from_dict]['AXNAME'] == F_dim:
                #print F_dim
                reconstructed_dict[F_dim] = attr_dic[axis_from_dict]
    return reconstructed_dict


def extract_attr_from_dic(attr_dic, F_dims):
    res_dict = {}

    dict_by_axis_names = reconstruct_dict(attr_dic, F_dims)
    #print len(dict_by_axis_names)

    for F in dict_by_axis_names:
        #print F
        d = dict_by_axis_names[F]

        res_dict[F] = {}
        
        SW = d['SW_p'] / d['SF']
        OFFSET = d['OFFSET']
        zero_ppm = OFFSET-SW
        SI = d['SI']
        axis_in_ppm = np.linspace(OFFSET,zero_ppm,SI)

        res_dict[F]['SW'] = SW
        res_dict[F]['OFFSET'] = OFFSET
        res_dict[F]['zero_ppm'] = zero_ppm
        res_dict[F]['SI'] = SI
        res_dict[F]['axis_in_ppm'] = axis_in_ppm
    

    #print res_dict
    return res_dict



class SpectrumObject_2D():
    """Not Commplete"""
    def init_spec_data(s):
        spectrum_path_dict = get_dict_of_spectra_type_with_paths()
        src = spectrum_path_dict[s.spec_type]
        attr_dic, spectrum_array = read_Bruker_2D(src)
        return attr_dic, spectrum_array
    
    def init_attributes(s):
        #test_extracting_attr_from_dic(s.attr_dic)
        res_dict = extract_attr_from_dic(s.attr_dic, ['F2', 'F1'])
        s.F1_dict = res_dict['F1']
        s.F2_dict = res_dict['F2']
        s.x_left = s.F2_dict['OFFSET']
        s.x_right = s.F2_dict['zero_ppm']
        s.x_axis = s.F2_dict['axis_in_ppm']
        s.y_top = s.F1_dict['zero_ppm']
        s.y_bottom = s.F1_dict['OFFSET']
        s.y_axis = s.F1_dict['axis_in_ppm']
    
    def __init__(s, spec_type):
        s.spec_type = spec_type
        s.attr_dic, s.spectrum_array = s.init_spec_data()
        s.init_attributes()




'''
class SpectrumObject_1D():
    """NotImplemented"""
    NotImplemented
    


class Spectrum_slice_1D():
    """needs:
    - ppm scale (x_axis)
    - ppm_ranges (x_min, x_max)
    - numpy_array_1D
    """
    NotImplemented

class Spectrum_slice_2D():
    """needs:
    - ppm scale (x_axis, y_axis)
    - ppm_ranges (x_min, x_max, y_min, y_max)
    - numpy_array_2D
    """
    NotImplemented

class Spectra_matrixes_and_data():
    """
    *
    """
    spec_slice_1D = Spectrum_slice_1D()
    spec_slice_2D = Spectrum_slice_2D()
#'''
