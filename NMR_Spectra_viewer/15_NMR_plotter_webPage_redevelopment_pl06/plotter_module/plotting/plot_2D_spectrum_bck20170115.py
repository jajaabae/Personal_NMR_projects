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

from plotter_module.plotting.construct_plot_composition import construct_plot_composition

def plot_2D_spectrum_from_object(intensity_multiplication_variable, spec_type, spec_obj, out_file_name, x_shifts, y_shifts, additional_plotting_settings=None):
        spectrum_array = spec_obj.spectrum_array
        xmin = spec_obj.x_left
        xmax = spec_obj.x_right
        ymin = spec_obj.y_top
        ymax = spec_obj.y_bottom
        axis_limits = [xmin, xmax, ymin, ymax]
        plot_marked_object_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, additional_plotting_settings=additional_plotting_settings)
        
def plot_2D_spectrum_from_array(intensity_multiplication_variable, spec_type, spectrum_array, out_file_name, x_shifts, y_shifts,  additional_plotting_settings=None):
    axis_limits = None
    plot_grid_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=False)

def overlay_grids(ax, height, width, plots_in_x_dir, plots_in_y_dir):
    def get_borders(width,plots_in_axis_direction):
        return np.linspace(0,width,plots_in_axis_direction+1)

    def get_center_crosses(width,plots_in_axis_direction):
        size_per_plot = float(width)/plots_in_axis_direction
        half = size_per_plot/2
        return np.linspace(half, width-half, plots_in_axis_direction)

    center_line_width = 1
    border_line_width = 5
    
    x_center_crosses = get_center_crosses(width, plots_in_x_dir)
    for b in x_center_crosses:
        ax.axvline(b, color='red', lw=center_line_width)
    y_center_crosses = get_center_crosses(height, plots_in_y_dir)
    for b in y_center_crosses:
        ax.axhline(b, color='red', lw=center_line_width)
            
    x_borders = get_borders(width,plots_in_x_dir)
    for b in x_borders:
        ax.axvline(b, color='black', lw=border_line_width)
    
    y_borders = get_borders(height,plots_in_y_dir)
    for b in y_borders:
        ax.axhline(b, color='black', lw=border_line_width)
    return ax
        
def contour_profile(plt):
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
    plt.register_cmap(name='test5', data=cdict5)  # optional lut kwarg
    return plt





def plot_marked_object_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=True, additional_plotting_settings=None):
    """OK
    Needs:
    - ...
    """
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
    
    contour_profile(plt)

    ax = fig.add_subplot(111)


    [xmin, xmax, ymin, ymax] = axis_limits
    width, height = spectrum_array.shape
    x_axis = np.linspace(xmin, xmax, width)
    y_axis = np.linspace(ymax, ymin, height)
    ax.contour(x_axis, y_axis, data, cl, cmap=plt.get_cmap('test5'))
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    if additional_plotting_settings:
        x = additional_plotting_settings[0]
        y = additional_plotting_settings[1]
        if not set_broad_squares:
            ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='1', markeredgecolor='black')
        else:
            ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='3', markeredgecolor='black')
        
    if not set_dpi:
        fig.savefig(out_file_name, bbox_inches='tight')
    else:
        dpi_value=35
        fig.savefig(out_file_name, dpi=dpi_value, bbox_inches='tight')


def plot_grid_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=True, additional_plotting_settings=None):
    """OK
    Needs:
    - ...
    """
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
    
    contour_profile(plt)

    ax = fig.add_subplot(111)


    ax.contour(data, cl, cmap=plt.get_cmap('test5'))
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.axis('off')

    ### grid-lines: ###
    width, height = data.shape
    plots_in_x_dir = len(x_shifts)
    plots_in_y_dir = len(y_shifts)
    overlay_grids(ax, width, height, plots_in_x_dir, plots_in_y_dir)

    if not set_dpi:
        fig.savefig(out_file_name, bbox_inches='tight', pad_inches = 0)
    else:
        fig.savefig(out_file_name, bbox_inches='tight', pad_inches = 0, dpi=dpi_value)


def plot_pairList_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=True, additional_plotting_settings=None):
    pass





if __name__ == '__main__':
    print 'test'
    width = 3
    plots_in_axis_direction = 3
    size_per_plot = float(width)/plots_in_axis_direction
    half = size_per_plot/2
    print np.linspace(half, width-half, plots_in_axis_direction)










###################################################################
### OLD/bck #######################################################
###################################################################
def plot_marked_object_spectrum(intensity_multiplication_variable, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=True, additional_plotting_settings=None):
    """OK
    Needs:
    - ...
    """
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
    
    contour_profile(plt)

    ax = fig.add_subplot(111)


    [xmin, xmax, ymin, ymax] = axis_limits
    width, height = spectrum_array.shape
    x_axis = np.linspace(xmin, xmax, width)
    y_axis = np.linspace(ymax, ymin, height)
    ax.contour(x_axis, y_axis, data, cl, cmap=plt.get_cmap('test5'))
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    if additional_plotting_settings:
        x = additional_plotting_settings[0]
        y = additional_plotting_settings[1]
        if not set_broad_squares:
            ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='1', markeredgecolor='black')
        else:
            ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='3', markeredgecolor='black')
        
    if not set_dpi:
        fig.savefig(out_file_name, bbox_inches='tight')
    else:
        dpi_value=35
        fig.savefig(out_file_name, dpi=dpi_value, bbox_inches='tight')
###################################################################
###################################################################

