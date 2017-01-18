class InformationObject():
    #pass
    def __init__(s):
        #custom variables
        s.cv_test = "Test OK!"

        ### Full plot: ###
        s.cv_x_from = .5#-0.5
        s.cv_x_to = 9.5#10.5
        s.cv_y_from = .5#-0.5
        s.cv_y_to = 9.5#10.5
        s.cv_separate_mult_value_for_fullPlot = 10
        s.axis_spec_x = 'PROTON'
        s.axis_spec_y = 'PROTON'

        """ ### H-C values ###
        s.cv_separate_mult_value_for_fullPlot = 180#160
        s.cv_y_from = 0#-0.5
        s.cv_y_to = 200#10.5
        s.axis_spec_x = 'PROTON'
        s.axis_spec_y = 'CARBON'
        #"""
		
        s.cv_full_plot_size_size_x = 20
        s.cv_full_plot_size_size_y = 20
        s.cv_full_top_1D_height_1D_horiz = 3
        s.cv_full_top_1D_height_labels_horiz = 1
        s.cv_full_left_1D_height_1D_verti = 3
        s.cv_full_left_1D_height_labels_verti = 1
		

        ### grid plot: ###
        s.cv_x_diameter_std = .3
        s.cv_y_diameter_std = s.cv_x_diameter_std
        s.cv_div_factor_x_1D_grid = 15#10
        s.cv_div_factor_y_1D_grid = s.cv_div_factor_x_1D_grid
        s.cv_center_line_width_grid2D = 0
        s.cv_border_line_width_grid2D = 3
        s.cv_center_line_width_grid_1D = 1
        s.cv_border_line_width_grid_1D = 3

        s.cv_grid_plot_size_size_x_and_y = 20
        s.cv_grid_plot_size_size_x = 20
        s.cv_grid_top_1D_height_1D_horiz = 3
        s.cv_grid_top_1D_height_labels_horiz = 1
        s.cv_grid_left_1D_height_1D_verti = 3
        s.cv_grid_left_1D_height_labels_verti = 2

        

        ### shared: ###
        s.cv_div_factor_x = 8
        s.cv_div_factor_y = 8
