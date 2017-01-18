import numpy as np

import matplotlib.pyplot as plt

def extract_1D_slice(spectrum_object_1D, x_coord_center, x_width):
    x_from, x_to = get_extraction_area_in_pixels(spectrum_object_1D, x_coord_center, x_width)
    
    spec_array_1D = spectrum_object_1D.spectrum_array
    spec_array_1D = spec_array_1D[x_from:x_to]

    return spec_array_1D

def extract_1D_slice_by_FromToValues(spectrum_object_1D, x_from, x_to):
    x_width = x_to - x_from
    coord_center = x_from + float(x_width)/2
    
    x_from, x_to = get_extraction_area_in_pixels(spectrum_object_1D, coord_center, x_width)
    
    spec_array_1D = spectrum_object_1D.spectrum_array
    spec_array_1D = spec_array_1D[x_from:x_to]
    
    return spec_array_1D

    

def get_extraction_area_in_pixels(spectrum_object_1D, x_coord, x_width):
    ppm_max = spectrum_object_1D.x_axis[0]
    ppm_min = spectrum_object_1D.x_axis[-1]
    pix_range = spectrum_object_1D.spectrum_array.shape[0] #Unknown X or Y
    #print 'pix_range', pix_range


    myList = np.linspace(ppm_max, ppm_min, pix_range)
    def get_pix_from_ppm(my_ppm_Number):
        result = min(myList, key=lambda x:abs(x-my_ppm_Number))
        pix_index = np.where(myList == result)[0][0]
        return pix_index
    #my_ppm_Number = 10
    #print get_pix_from_ppm(my_ppm_Number)

    #print get_pix_from_ppm(5)
    a = get_pix_from_ppm(5)
    b = get_pix_from_ppm( 5+float(x_width)/2. ) ##!! Cannot reach edges with a width of 3000! Why?
    radius_in_pix = a-b
    #print 'radius_in_pix', radius_in_pix

    x_pix_coord = get_pix_from_ppm(x_coord)
    #print y, x_coord, '=>', x_pix_coord
    
    x_from = x_pix_coord-radius_in_pix
    x_to = x_pix_coord+radius_in_pix

    #print 'x_pix_coord, radius_in_pix', x_pix_coord, radius_in_pix
    #print 'from, to', x_from, x_to

    if x_from < 0:
        x_from = 0
    if x_to > pix_range-1:
        x_to = pix_range-1

    return x_from, x_to #from/to. not x.


