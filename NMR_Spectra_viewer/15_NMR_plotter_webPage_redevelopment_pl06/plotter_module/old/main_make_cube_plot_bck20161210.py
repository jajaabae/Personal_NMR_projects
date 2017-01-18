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

def develop_make_cube_plot():
    instructions = {'AA': ['Arg4'],
                    'Spectra': ['ROESY'],
                    }
    sets_of_hydrogens = get_set_of_hydrogens_per_AA_per_spectrum(instructions)
    #print 'sets_of_hydrogens:', sets_of_hydrogens

    spectra_objects = get_nmr_spectra(instructions['Spectra'])
    
    #print spectra_objects

    ROESY_obj = spectra_objects['ROESY']


    #print ROESY_obj
    ###print ROESY_obj.spectrum_array.size
    #print ROESY_obj.spectrum_array.shape
    ##print ROESY_obj.spectrum_array
    #print ROESY_obj.x_left
    #print ROESY_obj.x_axis
    #print ROESY_obj.y_axis




    #out_file_name = 'roesy_2d.png'
    #plot_2D_spectrum_from_object('ROESY', ROESY_obj, out_file_name)


    import slice_combining.combine_cube_plot
    reload(slice_combining.combine_cube_plot)
    from slice_combining.combine_cube_plot import slicer_for_cube_plot
    
    group='native'
    width = 0.3
    #width = 1
    ###width = 3

    width = 0.15
    x_width = width
    y_width = width

    max_intensity = None
    draw_center_cross_with_val = max_intensity
    draw_outline_with_val = max_intensity
    
    the_set_of_H = sets_of_hydrogens['Arg4']['ROESY'][group]
    the_set_of_H =list(reversed(sorted(the_set_of_H)))
    x_set_of_atoms = the_set_of_H
    y_set_of_atoms = the_set_of_H
    array_extract_2D = slicer_for_cube_plot(ROESY_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, group, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)

    out_file_name = 'roesy_2d_cube.png'
    
    #print 'type(array_extract_2D)', type(array_extract_2D)
    #print 'array_extract_2D.shape', array_extract_2D.shape
    #print 'type(array_extract_2D[0][0])', type(array_extract_2D[0][0])

    plot_2D_spectrum_from_array('ROESY', array_extract_2D, out_file_name)





if __name__ == '__main__':
    #test_a()
    develop_make_cube_plot()
    



