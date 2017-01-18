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
from plotter_module.slicers.extract_1D_slice import extract_1D_slice_by_FromToValues

from plotter_module.slice_combining.combine_1D_slices_plot import combine_1D_slices_plot

def plot_2D_spectrum_from_object(information_instance, intensity_multiplication_variable, spec_type, spec_obj, spec_obj_1D_x_axis, spec_obj_1D_y_axis, out_file_name, x_shifts, y_shifts, additional_plotting_settings=None):
        spectrum_array = spec_obj.spectrum_array
        xmin = spec_obj.x_left
        xmax = spec_obj.x_right
        ymin = spec_obj.y_top
        ymax = spec_obj.y_bottom
        axis_limits = [xmin, xmax, ymin, ymax]
        plot_marked_object_spectrum(information_instance, intensity_multiplication_variable, spec_obj_1D_x_axis, spec_obj_1D_y_axis, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, additional_plotting_settings=additional_plotting_settings)
        
def plot_2D_spectrum_from_array(information_instance, intensity_multiplication_variable, spec_type, spectrum_array, spec_obj_1D_x_axis, spec_obj_1D_y_axis, out_file_name, x_shifts, y_shifts,  additional_plotting_settings=None):
    axis_limits = None
    plot_grid_spectrum(information_instance, intensity_multiplication_variable, spectrum_array, spec_obj_1D_x_axis, spec_obj_1D_y_axis, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=False)

def overlay_grids(information_instance, ax, height, width, plots_in_x_dir, plots_in_y_dir):
    def get_borders(width,plots_in_axis_direction):
        return np.linspace(0,width,plots_in_axis_direction+1)

    def get_center_crosses(width,plots_in_axis_direction):
        size_per_plot = float(width)/plots_in_axis_direction
        half = size_per_plot/2
        return np.linspace(half, width-half, plots_in_axis_direction)

    #center_line_width = 1
    #center_line_width = 0 ### TMP POS ###
    #border_line_width = 5 ### TMP POS ###
    center_line_width = information_instance.cv_center_line_width_grid2D
    border_line_width = information_instance.cv_border_line_width_grid2D
    
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




def plot_marked_object_spectrum(information_instance, intensity_multiplication_variable, spec_obj_1D_x_axis, spec_obj_1D_y_axis, spectrum_array, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=True, additional_plotting_settings=None):
    """OK
    Needs:
    - ...
    """
    try:
        intensity_multiplication_variable = float(intensity_multiplication_variable)
    except:
        print 'error: intensity_multiplication_variable'
        intensity_multiplication_variable = 10

    ### OVERRIDING! ###
    intensity_multiplication_variable = information_instance.cv_separate_mult_value_for_fullPlot

    sensitivity_adjusted___intensity_multiplication_variable = intensity_multiplication_variable/10
    
    data = spectrum_array
    cl = data.std() * 1.6 * sensitivity_adjusted___intensity_multiplication_variable * 0.73 ** np.arange(10)
    cl = np.concatenate((cl, cl*-1))

    fig = plt.figure()
    contour_profile(plt)
    #ax = fig.add_subplot(111)
    #ax0, top, left, main = construct_plot_composition(plt)
    """
    size_x_and_y = (20, 20)
    height_1D = 3
    height_labels = 2
    #ax0, top, left, ax, right, bot = construct_plot_composition(plt, size_x_and_y, height_1D, height_labels)
    height_1D_horiz = height_1D
    height_labels_horiz = height_labels
    height_1D_verti = height_1D
    height_labels_verti = height_labels
    #"""
    size_x_and_y = (information_instance.cv_full_plot_size_size_x, information_instance.cv_full_plot_size_size_y)
    height_1D_horiz = information_instance.cv_full_top_1D_height_1D_horiz
    height_labels_horiz = information_instance.cv_full_top_1D_height_labels_horiz
    height_1D_verti = information_instance.cv_full_left_1D_height_1D_verti
    height_labels_verti = information_instance.cv_full_left_1D_height_labels_verti
	
    ax0, top, left, ax, right, bot = construct_plot_composition(plt, size_x_and_y, height_1D_horiz, height_labels_horiz, height_1D_verti, height_labels_verti)
    

    #spec_1D_extract_x_axis = spec_obj_1D_x_axis.spectrum_array
    #x_from, x_to = 0.7,2 ###### TMP!!! ######
    x_from, x_to = information_instance.cv_x_from, information_instance.cv_x_to
    #y_from, y_to = 0,200 ###### TMP!!! ######
    #y_from, y_to = 0.7,2 ###### TMP!!! ######
    y_from, y_to = information_instance.cv_y_from, information_instance.cv_y_to
    div_factor_x = information_instance.cv_div_factor_x
    div_factor_y = information_instance.cv_div_factor_y
    ###############axes.set_ylim([ymin,ymax])
    #left.set_ylim([y_from,y_to])
    
    #spec_1D_extract_x_axis = extract_1D_slice_by_FromToValues(spec_obj_1D_x_axis, x_from, x_to)
    spec_1D_extract_x_axis = extract_1D_slice_by_FromToValues(spec_obj_1D_y_axis, x_from, x_to)
    
    #spec_1D_extract_y_axis = spec_obj_1D_y_axis.spectrum_array
    spec_1D_extract_y_axis = extract_1D_slice_by_FromToValues(spec_obj_1D_y_axis, y_from, y_to)
    top.plot(spec_1D_extract_x_axis)
    #top.set_ylim([x_from,x_to])
    #print 'len(spec_1D_extract_x_axis)', len(spec_1D_extract_x_axis)
    top.set_xlim([0,len(spec_1D_extract_x_axis)])
    #print 'max(spec_1D_extract_x_axis)', max(spec_1D_extract_x_axis)
    top.set_ylim([2*-abs(min(spec_1D_extract_x_axis)), max(spec_1D_extract_x_axis)/div_factor_x])
    
    left.set_xlim([-max(spec_1D_extract_y_axis)/div_factor_y, 2*abs(min(spec_1D_extract_y_axis))])
    x = spec_1D_extract_y_axis
    y=np.arange(len(spec_1D_extract_y_axis))
    x=-x
    #left.set_ylim([y_from,y_to])
    #left.axis((5,15,0,20))
    y_width, = spec_1D_extract_y_axis.shape
    #print 'y_width', y_width
    left.set_ylim([0,y_width])
    """
    y_axis_for_left = np.linspace(y_to, y_from, y_width)
    #y_axis_for_left
    #left.axis.yticks(y_axis_for_left)
    #left.yaxis.set_ticks(y_axis_for_left, y_axis_for_left)
    #x_bad,my = np.array([0,1,2,3]), ['a', 'b', 'c', 'd']
    print 'y.shape', y.shape
    print 'y_axis_for_left.shape', y_axis_for_left.shape
    #y_axis_for_left = [str(e) for e in y_axis_for_left]
    #left.yaxis.set_ticks(y,y_axis_for_left)
    #left.yaxis.set_ticks(np.array([1,1000,2000]),['a', 'b', 'c'])
    #left.yticks(np.arange(y_from, y_to, 1000))
    #left.yaxis.set_ticks(np.arange(y_from, y_width, 20000))
    #left.yaxis.set_ticks(np.arange(y_from, y_width, 2000))
    
    
    
    pix_y = np.linspace(0, y_width, 10)
    ppm_y = np.linspace(y_from, y_to, 10)
    ppm_y = ['1','2','3','4','5','6','7','8','9','0']
    left.yaxis.set_ticks(pix_y, ppm_y)
    #left.yaxis.set_ticks(np.arange(y_from, y_width, 2000))
    #"""
    ##############################################################
    left.plot(x,y)
    
    
    [xmin, xmax, ymin, ymax] = axis_limits
    width, height = spectrum_array.shape
    x_axis = np.linspace(xmin, xmax, width)
    y_axis = np.linspace(ymax, ymin, height)
    ax.contour(x_axis, y_axis, data, cl, cmap=plt.get_cmap('test5'))
    #plt.gca().invert_xaxis()
    #plt.gca().invert_yaxis()
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.set_xlim([x_to, x_from])
    ax.set_ylim([y_to, y_from])
    

    if additional_plotting_settings:
        x = additional_plotting_settings[0]
        y = additional_plotting_settings[1]
        if not set_broad_squares:
            ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='1', markeredgecolor='black')
        else:
            ax.plot(x, y, 'bs', markerfacecolor='none', markersize=10, markeredgewidth='3', markeredgecolor='black')
        
    if not set_dpi:
        fig.savefig(out_file_name, bbox_inches='tight', pad_inches = 0)
    else:
        dpi_value=35
        fig.savefig(out_file_name, dpi=dpi_value, bbox_inches='tight', pad_inches = 0)


def overlay_grids_1D_horizontal(information_instance, ax, width, plots_in_x_dir):
    def get_borders(width,plots_in_axis_direction):
        return np.linspace(0,width,plots_in_axis_direction+1)
    def get_center_crosses(width,plots_in_axis_direction):
        size_per_plot = float(width)/plots_in_axis_direction
        half = size_per_plot/2
        return np.linspace(half, width-half, plots_in_axis_direction)

    center_line_width = information_instance.cv_center_line_width_grid_1D
    border_line_width = information_instance.cv_border_line_width_grid_1D
    
    x_center_crosses = get_center_crosses(width, plots_in_x_dir)
    for b in x_center_crosses:
        ax.axvline(b, color='red', lw=center_line_width)
    #y_center_crosses = get_center_crosses(height, plots_in_y_dir)
    #for b in y_center_crosses:
    #    ax.axhline(b, color='red', lw=center_line_width)
            
    x_borders = get_borders(width,plots_in_x_dir)
    for b in x_borders:
        ax.axvline(b, color='black', lw=border_line_width)
    
    #y_borders = get_borders(height,plots_in_y_dir)
    #for b in y_borders:
    #    ax.axhline(b, color='black', lw=border_line_width)
    return ax


def overlay_grids_1D_vertical(information_instance, ax, height, plots_in_y_dir):
    def get_borders(width,plots_in_axis_direction):
        return np.linspace(0,width,plots_in_axis_direction+1)
    def get_center_crosses(width,plots_in_axis_direction):
        size_per_plot = float(width)/plots_in_axis_direction
        half = size_per_plot/2
        return np.linspace(half, width-half, plots_in_axis_direction)

    center_line_width = information_instance.cv_center_line_width_grid_1D
    border_line_width = information_instance.cv_border_line_width_grid_1D
    
    #x_center_crosses = get_center_crosses(width, plots_in_x_dir)
    #for b in x_center_crosses:
    #    ax.axvline(b, color='red', lw=center_line_width)
    y_center_crosses = get_center_crosses(height, plots_in_y_dir)
    for b in y_center_crosses:
        ax.axhline(b, color='red', lw=center_line_width)
            
    #x_borders = get_borders(width,plots_in_x_dir)
    #for b in x_borders:
    #    ax.axvline(b, color='black', lw=border_line_width)
    
    y_borders = get_borders(height,plots_in_y_dir)
    for b in y_borders:
        ax.axhline(b, color='black', lw=border_line_width)
    return ax


def plot_grid_spectrum(information_instance, intensity_multiplication_variable, spectrum_array, spec_obj_1D_x_axis, spec_obj_1D_y_axis, axis_limits, out_file_name, x_shifts, y_shifts, with_axis=True, additional_plotting_settings=None):
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
    #size_x_and_y = (20, information_instance.cv_grid_plot_size_size_x)
    #height_1D = 4
    #height_labels = 2
    #ax0, top, left, ax, right, bot = construct_plot_composition(plt, size_x_and_y, height_1D, height_labels)
    #height_1D_horiz = height_1D
    #height_labels_horiz = height_labels
    #height_1D_verti = height_1D
    #height_labels_verti = height_labels
    size_x_and_y = (information_instance.cv_grid_plot_size_size_x_and_y, information_instance.cv_grid_plot_size_size_x)
    height_1D_horiz = information_instance.cv_grid_top_1D_height_1D_horiz
    height_labels_horiz = information_instance.cv_grid_top_1D_height_labels_horiz
    height_1D_verti = information_instance.cv_grid_left_1D_height_1D_verti
    height_labels_verti = information_instance.cv_grid_left_1D_height_labels_verti
    ax0, top, left, ax, right, bot = construct_plot_composition(plt, size_x_and_y, height_1D_horiz, height_labels_horiz, height_1D_verti, height_labels_verti)
  
    
    contour_profile(plt)

    #ax = fig.add_subplot(111)

    #print 'x_shifts', x_shifts
    #print 'len(x_shifts)', len(x_shifts)
    
    bot.set_xlim([0, len(x_shifts)])
    bot.set_ylim([2, 0])
    i=0
    for e in x_shifts:
        label = str(e)
        bot.text(i+0.5, 1, label, horizontalalignment='center', verticalalignment='center',
                 #bbox={'facecolor':'white', 'alpha':0.5, 'pad':0},
                 )
        i += 1
        
    #bot.text(1.5, 1, 'hi\nthere', style='italic', horizontalalignment='center',
    #    verticalalignment='center',bbox={'facecolor':'white', 'alpha':0.5, 'pad':0})
    


    #print 'y_shifts', y_shifts
    right.set_ylim([0, len(y_shifts)])
    right.set_xlim([2, 0])
    i=0
    for e in y_shifts:
        label = str(e)
        right.text(1, i+0.5, label, horizontalalignment='center', verticalalignment='center',
                 #bbox={'facecolor':'white', 'alpha':0.5, 'pad':0},
                 )
        i += 1




    #print spec_obj_1D_x_axis, spec_obj_1D_y_axis
    try:
        x_width = float(information_instance.x_diameter)
    except:
        x_width = float(information_instance.cv_x_diameter_std)
    spec_array_1D_x = combine_1D_slices_plot(spec_obj_1D_x_axis, x_shifts, x_width)

    width_x = len(spec_array_1D_x)
    plots_in_x_dir = len(x_shifts)
    top.set_xlim([0,width_x])
    top.set_ylim([2*-abs(min(spec_obj_1D_x_axis.spectrum_array)), max(spec_obj_1D_x_axis.spectrum_array)/information_instance.cv_div_factor_x_1D_grid])
    overlay_grids_1D_horizontal(information_instance, top, width_x, plots_in_x_dir)
    top.plot(spec_array_1D_x)


    try:
        y_width = float(information_instance.y_diameter)
    except:
        try:
            y_width = float(information_instance.x_diameter)
        except:
            y_width = float(information_instance.cv_y_diameter_std)
    spec_array_1D_y = combine_1D_slices_plot(spec_obj_1D_y_axis, y_shifts, y_width)
    x = spec_array_1D_y
    y=np.arange(len(spec_array_1D_y))
    x=-x
    y_width, = spec_array_1D_y.shape
    left.set_ylim([0,len(spec_array_1D_y)])
    left.set_xlim([ -max(spec_obj_1D_y_axis.spectrum_array)/information_instance.cv_div_factor_x_1D_grid, -2*-abs(min(spec_obj_1D_y_axis.spectrum_array)) ])

    width_y = len(spec_array_1D_y)
    plots_in_y_dir = len(y_shifts)
    overlay_grids_1D_vertical(information_instance, left, width_y, plots_in_y_dir)

    left.plot(x,y)





    ax.contour(data, cl, cmap=plt.get_cmap('test5'))
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.axis('off')

    ### grid-lines: ###
    width, height = data.shape
    plots_in_x_dir = len(x_shifts)
    plots_in_y_dir = len(y_shifts)
    overlay_grids(information_instance, ax, width, height, plots_in_x_dir, plots_in_y_dir)

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






