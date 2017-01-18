def webPage_requests_CreationOfROESYSpectra(
            datalists=None,
            x_list=None,
            y_list=None,
            x_diameter=0.3,
            y_diameter=None,
            spec_type=None,
            intensity_multiplication_variable=10,
            information_instance = None,
            ):
    if len(x_diameter)<=0:
        x_diameter=0.3
    if y_diameter == None or len(y_diameter)<=0 or len(y_list)<=0:
        y_diameter = x_diameter
    if y_list == None or len(y_list)<=0:
        y_list = x_list

    if intensity_multiplication_variable == None or len(intensity_multiplication_variable)<=0:
        intensity_multiplication_variable = 10

    x_diameter = float(x_diameter)
    y_diameter = float(y_diameter)

    #lists from strings
    x_list = ppm_listString_to_list(x_list)
    y_list = ppm_listString_to_list(y_list)

    x_list = sort_ppm_string(x_list)
    y_list = sort_ppm_string(y_list)


    #print x_list
    #print y_list

    from plotter_module.make_cube_plot_from_web_rquest import make_cube_plot_from_web_rquest
    #spec_type = 'ROESY'
    #spec_type = 'COSY'
    figureName, figureName2 = make_cube_plot_from_web_rquest(spec_type, x_list, y_list, x_diameter, y_diameter, intensity_multiplication_variable, information_instance)
    
    #figureName = 'another_tmp.png'
    #figureName2 = 'another2_tmp.png'    
    return figureName, figureName2

import re
def ppm_listString_to_list(list_string):
    ret=None
    def splitting(list_string):
        #list_string = '234,  65 34 43,3.1'
        a_list = re.split('[ ,]', list_string)
        b_list = filter(None, a_list)
        return b_list
    try:
        #ret = [float(e) for e in list_string.split(',')]
        ret = [float(e) for e in splitting(list_string)]
        print ret
    except:
        print 'Invalid ppm-string:', list_string
    return ret

def sort_ppm_string(ppm_list):
    sorted_list = list(reversed(sorted(ppm_list)))
    return sorted_list
