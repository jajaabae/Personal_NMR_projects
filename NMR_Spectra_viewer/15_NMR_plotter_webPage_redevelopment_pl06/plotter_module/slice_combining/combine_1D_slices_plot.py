from plotter_module.slicers.extract_1D_slice import extract_1D_slice
import numpy as np


def combine_1D_slices_plot(spec_obj, x_set_of_atoms, x_width):
    """NotImplemented"""

    #array_1D = spec_obj.spectrum_array

    the_set_of_H = x_set_of_atoms


    cells_of_1D_cells = []
    for j in range(len(the_set_of_H)):
        #cells_of_2D_cells.append( (the_set_of_H[i], the_set_of_H[j]) )
        x_coord = float(the_set_of_H[j])
        array_1D = extract_1D_slice(spec_obj, x_coord, x_width)
        cells_of_1D_cells.append( array_1D )

    concatination_of_1D_cells = np.concatenate(cells_of_1D_cells, axis=1)
    #rows_of_2D_cells.append(cells_of_2D_cells)
    #rows_of_2D_cells = np.concatenate(rows_of_2D_cells, axis=0)

    return concatination_of_1D_cells



