import numpy as np

from get_NMR_data.read_Bruker_2D import read_Bruker_2D
from data_containers.SpectrumObjects import SpectrumObject_2D
#from plotting.plot_ROESY_spectrum import plot_ROESY_spectrum

from hydrogens_per_AA_per_spectrum.get_set_of_hydrogens_per_AA_per_spectrum import get_set_of_hydrogens_per_AA_per_spectrum #pck


import get_NMR_data.get_nmr_spectra
reload(get_NMR_data.get_nmr_spectra)
from get_NMR_data.get_nmr_spectra import get_nmr_spectra


import plotting.plot_2D_spectrum
reload(plotting.plot_2D_spectrum)
from plotting.plot_2D_spectrum import plot_2D_spectrum_from_object
from plotting.plot_2D_spectrum import plot_2D_spectrum_from_array


def test_a():
    src = 'Bruker_NMR_spectra/23/pdata/1'
    attr_dic, spectrum_array = read_Bruker_2D(src)
    
    a = SpectrumObject_2D(attr_dic, spectrum_array)
    out_file_name = 'roesy_2d.png'
    plot_ROESY_spectrum(a.spectrum_array, out_file_name)

import slicers.extract_2D_slice
reload(slicers.extract_2D_slice)
from slicers.extract_2D_slice import extract_2D_slice

import slice_combining.combine_cube_plot
reload(slice_combining.combine_cube_plot)
from slice_combining.combine_cube_plot import slicer_for_cube_plot

import itertools

def develop_make_cube_plot():
    instructions = {'AA': ['Arg4'],
                    'Spectra': ['ROESY'],
                    }
    sets_of_hydrogens = get_set_of_hydrogens_per_AA_per_spectrum(instructions)
    spectra_objects = get_nmr_spectra(instructions['Spectra'])
    ROESY_obj = spectra_objects['ROESY']
    
    
    width = 0.3
    #width = 1
    ###width = 3
    width = 0.15
    x_width = width
    y_width = width

    #YMAX_p 570030888
    #YMIN_p -27070504
    max_intensity = 570030888
    min_intensity = -27070504
    draw_center_cross_with_val = max_intensity/4 #not in use
    draw_outline_with_val = -min_intensity/100


    group_pairs = [
        ('native', 'native'),
        ('correlated', 'correlated'),
        ]

    for group_pair in group_pairs:
        #group_pair = group_pairs[0]
        spec_type = 'ROESY'
        AA = 'Arg4'
        
        x_set_of_atoms, y_set_of_atoms = get_sets_of_hydrogens_for_cube_plot(sets_of_hydrogens, group_pair)
        out_file_name = ''+spec_type+'_'+AA+'_2D_cube_'+group_pair[0]+'_'+group_pair[1]+'_marked.png'
        prod = list(itertools.product(x_set_of_atoms, y_set_of_atoms))
        x_set = [e[0] for e in prod]
        y_set = [e[1] for e in prod]
        additional_plotting_settings = (x_set, y_set)
        
        plot_2D_spectrum_from_object(spec_type, ROESY_obj, out_file_name, additional_plotting_settings=additional_plotting_settings)
        array_extract_2D = slicer_for_cube_plot(ROESY_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)

        
        
        out_file_name = ''+spec_type+'_'+AA+'_2D_cube_'+group_pair[0]+'_'+group_pair[1]+'_.png'
        plot_2D_spectrum_from_array('ROESY', array_extract_2D, out_file_name)



def get_sets_of_hydrogens_for_cube_plot(sets_of_hydrogens, group_pair):
    x_set_of_atoms = sets_of_hydrogens['Arg4']['ROESY'][group_pair[0]]
    x_set_of_atoms =list(reversed(sorted(x_set_of_atoms)))
    y_set_of_atoms = sets_of_hydrogens['Arg4']['ROESY'][group_pair[1]]
    y_set_of_atoms =list(reversed(sorted(y_set_of_atoms)))
    return x_set_of_atoms, y_set_of_atoms



if __name__ == '__main__':
    #test_a()
    develop_make_cube_plot()
    



