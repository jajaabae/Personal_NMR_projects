import numpy as np

from plotter_module.get_NMR_data.read_Bruker_2D import read_Bruker_2D
from plotter_module.data_containers.SpectrumObjects import SpectrumObject_2D
#from plotting.plot_ROESY_spectrum import plot_ROESY_spectrum

from plotter_module.hydrogens_per_AA_per_spectrum.get_set_of_hydrogens_per_AA_per_spectrum import get_set_of_hydrogens_per_AA_per_spectrum #pck

from plotter_module.get_NMR_data.get_nmr_spectra import get_nmr_spectra
from plotter_module.get_NMR_data.get_Bruker_data_1D import get_Bruker_data_1D

import plotter_module.plotting.plot_2D_spectrum
reload(plotter_module.plotting.plot_2D_spectrum)
from plotter_module.plotting.plot_2D_spectrum import plot_2D_spectrum_from_object
from plotter_module.plotting.plot_2D_spectrum import plot_2D_spectrum_from_array
from plotter_module.slicers.extract_2D_slice import extract_2D_slice

from plotter_module.slice_combining.combine_cube_plot import slicer_for_cube_plot
from plotter_module.slice_combining.combine_cube_plot import slicer_for_cube_plot_unEven

import itertools


def make_cube_plot_from_web_rquest(spec_type, x_list, y_list, x_diameter, y_diameter, intensity_multiplication_variable, information_instance):
    x_set_of_atoms, y_set_of_atoms = x_list, y_list
    out_path = 'static/'


    if x_set_of_atoms == y_set_of_atoms:
        H_and_C = False
    else:
        H_and_C = True

    #spec_type = 'ROESY'
    AA = ''
    group_pair=['','']
    spectra_objects = get_nmr_spectra([spec_type])
    #print spectra_objects, '***'
    spec_obj = spectra_objects[spec_type]

    #axis_spec_x = 'PROTON'
    #axis_spec_y = 'PROTON'
    axis_spec_x = information_instance.axis_spec_x
    axis_spec_y = information_instance.axis_spec_y
    #spec_obj_1D_x_axis = get_Bruker_data_1D('PROTON')
    spec_obj_1D_x_axis = get_Bruker_data_1D(axis_spec_x)
    #spec_obj_1D_y_axis = get_Bruker_data_1D('CARBON')
    #spec_obj_1D_y_axis = get_Bruker_data_1D('PROTON')
    spec_obj_1D_y_axis = get_Bruker_data_1D(axis_spec_y)


    x_width = x_diameter
    y_width = y_diameter

    #YMAX_p 570030888
    #YMIN_p -27070504
    max_intensity = 570030888
    min_intensity = -27070504
    draw_center_cross_with_val = max_intensity/4 #not in use
    #draw_outline_with_val = -min_intensity/100
    if not H_and_C:
        draw_outline_with_val = -min_intensity/10
    else:
        #draw_outline_with_val = -min_intensity/1
        draw_outline_with_val = -min_intensity/5
    
    out_file_name = ''+spec_type+'_'+'_2D_cube_'+'_marked.png'
    prod = list(itertools.product(x_set_of_atoms, y_set_of_atoms))
    x_set = [e[0] for e in prod]
    y_set = [e[1] for e in prod]
    additional_plotting_settings = (x_set, y_set) 
    out_file_in_path = out_path+out_file_name
    plot_2D_spectrum_from_object(information_instance, intensity_multiplication_variable, spec_type, spec_obj, spec_obj_1D_x_axis, spec_obj_1D_y_axis, out_file_in_path, x_set_of_atoms, y_set_of_atoms, additional_plotting_settings=additional_plotting_settings)

    print 'x_set_of_atoms:', x_set_of_atoms
    print 'y_set_of_atoms:', y_set_of_atoms
    print 'x_set:', x_set
    print 'y_set:', y_set

    if not H_and_C:
        array_extract_2D = slicer_for_cube_plot(spec_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)
    else:
        array_extract_2D = slicer_for_cube_plot_unEven(spec_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)
    out_file_name2 = ''+spec_type+'_'+'_2D_cube_'+'_.png'
    out_file_in_path2 = out_path+out_file_name2
    plot_2D_spectrum_from_array(information_instance, intensity_multiplication_variable, spec_type, array_extract_2D, spec_obj_1D_x_axis, spec_obj_1D_y_axis, out_file_in_path2, x_set_of_atoms, y_set_of_atoms, )

    #return out_file_name.split('/')[1], out_file_name2.split('/')[1]
    return out_file_name, out_file_name2




if __name__ == '__main__':
    pass    



