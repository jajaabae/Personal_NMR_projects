import numpy as np

def extract_2D_slice(spectrum_object_2D, x_coord, x_width, y_coord, y_width):
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
    






