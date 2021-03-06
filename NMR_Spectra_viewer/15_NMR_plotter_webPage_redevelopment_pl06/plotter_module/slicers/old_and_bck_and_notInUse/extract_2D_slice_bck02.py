import numpy as np


def get_extraction_area_in_pixels(spectrum_object_2D, x_coord, x_width):
    ppm_max = spectrum_object_2D.x_axis[0]
    ppm_min = spectrum_object_2D.x_axis[-1]

    pix_range = spectrum_object_2D.spectrum_array.shape[0] #Unknown X or Y
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
    
    x_from = x_pix_coord-radius_in_pix
    x_to = x_pix_coord+radius_in_pix

    #print 'x_pix_coord, radius_in_pix', x_pix_coord, radius_in_pix
    #print 'from, to', x_from, x_to

    if x_from < 0:
        x_from = 0
    if x_to > pix_range-1:
        x_to = pix_range-1

    return x_from, x_to #from/to. not x.


def extract_2D_slice(spectrum_object_2D, x_coord, x_width, y_coord, y_width):
    """NotImplemented"""

    x_from, x_to = get_extraction_area_in_pixels(spectrum_object_2D, x_coord, x_width)
    y_from, y_to = get_extraction_area_in_pixels(spectrum_object_2D, y_coord, y_width)
    
    #print x_from, x_to, y_from, y_to
    spec_array_2D = spectrum_object_2D.spectrum_array
    spec_array_2D = spec_array_2D[x_from:x_to, y_from:y_to]
    #print spec_array_2D
    #print spec_array_2D.shape
    
    return spec_array_2D
    








def old2_extract_2D_slice(spectrum_object_2D, x_coord, x_width, y_coord, y_width):
    """NotImplemented"""
    ppm_max = spectrum_object_2D.x_axis[0]
    ppm_min = spectrum_object_2D.x_axis[-1]

    pix_range = spectrum_object_2D.spectrum_array.shape[0] #Unknown X or Y
    print 'pix_range', pix_range

    myList = np.linspace(ppm_max, ppm_min, pix_range)
    def get_pix_from_ppm(my_ppm_Number):
        result = min(myList, key=lambda x:abs(x-my_ppm_Number))
        pix_index = np.where(myList == result)[0][0]
        return pix_index
    #my_ppm_Number = 10
    #print get_pix_from_ppm(my_ppm_Number)

    print get_pix_from_ppm(5)
    a = get_pix_from_ppm(5)
    b = get_pix_from_ppm( 5+float(x_width)/2. )
    radius_in_pix = a-b
    print radius_in_pix

    x_pix_coord = get_pix_from_ppm(x_coord)
    #y_pix_coord = 
    
    x_from = x_pix_coord-radius_in_pix
    x_to = x_pix_coord+radius_in_pix
    
    y_from = x_from #TMP
    y_to = x_to #TMP

    print x_from, x_to, y_from, y_to
    spec_array_2D = spectrum_object_2D.spectrum_array
    spec_array_2D = spec_array_2D[x_from:x_to, y_from:y_to]
    print spec_array_2D
    print spec_array_2D.shape
    
    return spec_array_2D
    





def old_extract_2D_slice(spectrum_object_2D, x_coord, x_width, y_coord, y_width):
    """NotImplemented"""
    print spectrum_object_2D
    print spectrum_object_2D.spectrum_array.shape
    #print spectrum_object_2D.x_axis
    ppm_max = spectrum_object_2D.x_axis[0]
    ppm_min = spectrum_object_2D.x_axis[-1]
    ppm_range = ppm_max-ppm_min
    print 'ppm_range', ppm_range

    pix_range = spectrum_object_2D.spectrum_array.shape[0] #Unknown X or Y
    print 'pix_range', pix_range

    def calc_pix_from_ppm(pix_range, ppm_range, ppm_val): #!NotPerfect!!
        pix_per_ppm = float(pix_range)/float(ppm_range)
        #print 'pix_per_ppm', pix_per_ppm
        number_of_pixels = pix_per_ppm*ppm_val
        return pix_range-number_of_pixels
    #print calc_pix_from_ppm(pix_range, ppm_range, ppm_max)
    #print calc_pix_from_ppm(pix_range, ppm_range, 5)
    #print calc_pix_from_ppm(pix_range, ppm_range, ppm_min)
    
    print np.linspace(ppm_max, ppm_min, pix_range).shape
    myList = np.linspace(ppm_max, ppm_min, pix_range)
    print myList

    #print np.linspace(0, pix_range, pix_range).shape
    #print np.linspace(0, pix_range, pix_range)


    
    def get_pix_from_ppm(my_ppm_Number):
        result = min(myList, key=lambda x:abs(x-my_ppm_Number))
        #print result
        #print result in myList
        pix_index = np.where(myList == result)[0][0]
        return pix_index
        
    my_ppm_Number = 10
    print get_pix_from_ppm(my_ppm_Number)
    
    print '*'
    


