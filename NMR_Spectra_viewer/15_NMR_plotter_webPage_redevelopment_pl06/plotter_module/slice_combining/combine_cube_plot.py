import plotter_module.slicers.extract_2D_slice
reload(plotter_module.slicers.extract_2D_slice)
from plotter_module.slicers.extract_2D_slice import extract_2D_slice


import numpy as np

"""
def add_cross_and_borders(array_2D, draw_center_cross_with_val=None, draw_outline_with_val=None):
    array_2D = np.copy(array_2D)
    if draw_outline_with_val:
        array_2D[0,:]=draw_outline_with_val
        array_2D[:,0]=draw_outline_with_val
    return array_2D
#"""

def slicer_for_cube_plot(spec_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, draw_center_cross_with_val=None, draw_outline_with_val=None):
    """NotImplemented"""

    array_2D = spec_obj.spectrum_array

    the_set_of_H = x_set_of_atoms

    rows_of_2D_cells = []
    for i in range(len(the_set_of_H)):
        cells_of_2D_cells = []
        for j in range(len(the_set_of_H)):
            #cells_of_2D_cells.append( (the_set_of_H[i], the_set_of_H[j]) )
            x_coord = the_set_of_H[i]
            y_coord = the_set_of_H[j]
            array_2D = extract_2D_slice(spec_obj, x_coord, x_width, y_coord, y_width)
            #array_2D = add_cross_and_borders(array_2D, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)
            cells_of_2D_cells.append( array_2D )

        cells_of_2D_cells = np.concatenate(cells_of_2D_cells, axis=1)
        rows_of_2D_cells.append(cells_of_2D_cells)
    rows_of_2D_cells = np.concatenate(rows_of_2D_cells, axis=0)

    return rows_of_2D_cells



'''
def slice_cube(MAT, width, height, ppm):
    """NotImplemented"""
    NotImplemented
#'''


def slicer_for_cube_plot_unEven(spec_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, draw_center_cross_with_val=None, draw_outline_with_val=None):
    """NotImplemented"""

    '''
    print """**************************************
**************************************
**************************************"""
#'''


    array_2D = spec_obj.spectrum_array

    the_set_of_H = x_set_of_atoms
    the_set_of_C = y_set_of_atoms

    #print len(the_set_of_H), the_set_of_H
    #print len(the_set_of_C), the_set_of_C
    
    rows_of_2D_cells = []
    for i in range(len(the_set_of_C)):
        cells_of_2D_cells = []
        for j in range(len(the_set_of_H)):
            #cells_of_2D_cells.append( (the_set_of_H[i], the_set_of_H[j]) )
            x_coord = the_set_of_H[j]
            y_coord = the_set_of_C[i]
            #array_2D = extract_2D_slice(spec_obj, x_coord, x_width, y_coord, y_width)
            array_2D = extract_2D_slice(spec_obj, y_coord, y_width, x_coord, x_width)
            #array_2D = add_cross_and_borders(array_2D, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)
            cells_of_2D_cells.append( array_2D )

        cells_of_2D_cells = np.concatenate(cells_of_2D_cells, axis=1)
        rows_of_2D_cells.append(cells_of_2D_cells)
    rows_of_2D_cells = np.concatenate(rows_of_2D_cells, axis=0)

    return rows_of_2D_cells


















def bck_slicer_for_cube_plot_unEven(spec_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, draw_center_cross_with_val=None, draw_outline_with_val=None):
    """NotImplemented"""

    print """**************************************
**************************************
**************************************"""


    array_2D = spec_obj.spectrum_array

    the_set_of_H = x_set_of_atoms
    the_set_of_C = y_set_of_atoms

    print len(the_set_of_H), the_set_of_H
    print len(the_set_of_C), the_set_of_C
    print
    print 
    print

    rows_of_2D_cells = []
    for i in range(len(the_set_of_H)):
        cells_of_2D_cells = []
        for j in range(len(the_set_of_C)):
            #cells_of_2D_cells.append( (the_set_of_H[i], the_set_of_H[j]) )
            x_coord = the_set_of_H[i]
            y_coord = the_set_of_C[j]
            array_2D = extract_2D_slice(spec_obj, x_coord, x_width, y_coord, y_width)
            array_2D = add_cross_and_borders(array_2D, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)
            cells_of_2D_cells.append( array_2D )

        cells_of_2D_cells = np.concatenate(cells_of_2D_cells, axis=1)
        rows_of_2D_cells.append(cells_of_2D_cells)
    rows_of_2D_cells = np.concatenate(rows_of_2D_cells, axis=0)

    return rows_of_2D_cells





