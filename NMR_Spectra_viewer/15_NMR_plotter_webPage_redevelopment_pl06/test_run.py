import plotter_module.make_cube_plot_from_web_rquest
reload(plotter_module.make_cube_plot_from_web_rquest)
from plotter_module.make_cube_plot_from_web_rquest import make_cube_plot_from_web_rquest

x_list = [9,8,7,6,5,4,3,2,1]
y_list = x_list
x_diameter = 0.2
y_diameter = x_diameter
spec_type = 'ROESY'
spec_type = 'COSY'
spec_type = 'TOCSY'

make_cube_plot_from_web_rquest(spec_type, x_list, y_list, x_diameter, y_diameter)


