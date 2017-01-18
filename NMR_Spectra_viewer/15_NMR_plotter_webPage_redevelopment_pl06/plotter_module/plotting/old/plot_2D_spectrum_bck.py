import numpy as np
import matplotlib.pyplot as plt
#dpi_value=None
#dpi_value=50
#dpi_value=40
#dpi_value=35
##dpi_value=36
set_dpi=True
set_dpi=False
set_broad_squares=True

def plot_2D_spectrum_from_object(intensity_multiplication_variable, spec_type, spec_obj, out_file_name, additional_plotting_settings=None):
    if spec_type == 'ROESY':
        spectrum_array = spec_obj.spectrum_array
        #x_axis = spec_obj.x_axis
        #y_axis = spec_obj.y_axis
        xmin = spec_obj.x_left
        xmax = spec_obj.x_right
        ymin = spec_obj.y_top
        ymax = spec_obj.y_bottom
        axis_limits = [xmin, xmax, ymin, ymax]
        plot_ROESY_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, additional_plotting_settings=additional_plotting_settings)
    else:
        spectrum_array = spec_obj.spectrum_array
        #x_axis = spec_obj.x_axis
        #y_axis = spec_obj.y_axis
        xmin = spec_obj.x_left
        xmax = spec_obj.x_right
        ymin = spec_obj.y_top
        ymax = spec_obj.y_bottom
        axis_limits = [xmin, xmax, ymin, ymax]
        plot_ROESY_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, additional_plotting_settings=additional_plotting_settings)
    
        

def plot_2D_spectrum_from_array(intensity_multiplication_variable, spec_type, spectrum_array, out_file_name, additional_plotting_settings=None):
    axis_limits = None
    if spec_type == 'ROESY':
        plot_ROESY_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, with_axis=False)
    else:
        plot_ROESY_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, with_axis=False)
        

def plot_ROESY_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, with_axis=True, additional_plotting_settings=None):
    """OK
    Needs:
    - ...
    """
    #intensity_multiplication_variable = 1
    #intensity_multiplication_variable = 50
    #intensity_multiplication_variable = 30

    #intensity_multiplication_variable = 80
    ##intensity_multiplication_variable = 20
    #intensity_multiplication_variable = 100
    
    try:
        intensity_multiplication_variable = float(intensity_multiplication_variable)
    except:
        print 'error: intensity_multiplication_variable'
        intensity_multiplication_variable = 10
    sensitivity_adjusted___intensity_multiplication_variable = intensity_multiplication_variable/10
    
    data = spectrum_array
    cl = data.std() * 1.6 * sensitivity_adjusted___intensity_multiplication_variable * 0.73 ** np.arange(10)
    cl = np.concatenate((cl, cl*-1))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    cdict5 = {'red':   ((0.0,  1.0, 1.0),
                       (0.49, 1.0, 1.0),
                       (0.5, 0.0, 0.0),
                       (1.0,  0.0, 0.0)),

             'green': ((0.0,  0.0, 0.0),
                       (1.0,  0.0, 0.0)),
              
             'blue':  ((0.0,  0.0, 0.0),
                       (0.5, 0.0, 0.0),
                       (0.51, 1.0, 1.0),
                       (1.0,  1.0, 1.0))}

    #ax.axis(axis_limits)
    plt.register_cmap(name='test5', data=cdict5)  # optional lut kwarg

    #ax.axis(axis_limits)
    
    #ax.contour(data, cl, cmap=plt.get_cmap('test5'))


    if with_axis:
        [xmin, xmax, ymin, ymax] = axis_limits
        #print xmin, xmax, 2048
        #print np.linspace(xmin, xmax, 2048)
        x_axis = np.linspace(xmin, xmax, 2048)
        #y_axis = np.linspace(ymin, ymax, 2048)
        y_axis = np.linspace(ymax, ymin, 2048)
        ax.contour(x_axis, y_axis, data, cl, cmap=plt.get_cmap('test5'))
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        
        #ax.plot([2, 3], [3, 4], 'bo', markerfacecolor='none', markersize=15, markeredgewidth='3', markeredgecolor='black')
        if additional_plotting_settings:
            x = additional_plotting_settings[0]
            y = additional_plotting_settings[1]
            if not set_broad_squares:
                ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='1', markeredgecolor='black')
            else:
                ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='3', markeredgecolor='black')
        

        if not set_dpi:
            fig.savefig(out_file_name)
        else:
            dpi_value=35
            fig.savefig(out_file_name, dpi=dpi_value)
    else:
        ax.contour(data, cl, cmap=plt.get_cmap('test5'))
        ax.axis('off')

        if not set_dpi:
            fig.savefig(out_file_name, bbox_inches='tight', pad_inches = 0)
        else:
            dpi_value=36
            dpi_value=37
            fig.savefig(out_file_name, bbox_inches='tight', pad_inches = 0, dpi=dpi_value)

    
    
    ###out_file_name = 'roesy_2d.png'
    #fig.savefig(out_file_name)





