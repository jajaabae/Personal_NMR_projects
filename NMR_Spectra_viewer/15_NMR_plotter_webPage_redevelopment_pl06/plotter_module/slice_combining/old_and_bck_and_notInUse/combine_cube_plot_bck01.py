import plotter_module.slicers.extract_2D_slice
reload(plotter_module.slicers.extract_2D_slice)
from plotter_module.slicers.extract_2D_slice import extract_2D_slice


import numpy as np #used in old test functions


def add_cross_and_borders(array_2D, draw_center_cross_with_val=None, draw_outline_with_val=None):
    array_2D = np.copy(array_2D)
    #print draw_outline_with_val
    if draw_outline_with_val:
        #print array_2D.shape
        array_2D[0,:]=draw_outline_with_val
        array_2D[:,0]=draw_outline_with_val

    return array_2D


#def slicer_for_cube_plot(spec_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, group, draw_center_cross_with_val=None, draw_outline_with_val=None):
def slicer_for_cube_plot(spec_obj, x_set_of_atoms, y_set_of_atoms, x_width, y_width, draw_center_cross_with_val=None, draw_outline_with_val=None):
    """NotImplemented"""
    #sets_of_hydrogens
    
    array_2D = spec_obj.spectrum_array
    #the_set_of_H = sets_of_hydrogens['Arg4']['ROESY'][group]
    #the_set_of_H = sorted(the_set_of_H)
    #the_set_of_H = list(reversed(the_set_of_H))
    #print the_set_of_H
    #print 'type(the_set_of_H)', type(the_set_of_H)

    #x_coord = x_set_of_atoms[5]
    #y_coord = y_set_of_atoms[5]
    #array_extract_2D = extract_2D_slice(spec_obj, x_coord, x_width, y_coord, y_width)

    the_set_of_H = x_set_of_atoms


    #test_mesh5()
    rows_of_2D_cells = []
    for i in range(len(the_set_of_H)):
        cells_of_2D_cells = []
        for j in range(len(the_set_of_H)):
            #cells_of_2D_cells.append( (the_set_of_H[i], the_set_of_H[j]) )
            x_coord = the_set_of_H[i]
            y_coord = the_set_of_H[j]
            array_2D = extract_2D_slice(spec_obj, x_coord, x_width, y_coord, y_width)
            array_2D = add_cross_and_borders(array_2D, draw_center_cross_with_val=draw_center_cross_with_val, draw_outline_with_val=draw_outline_with_val)
            cells_of_2D_cells.append( array_2D )

        cells_of_2D_cells = np.concatenate(cells_of_2D_cells, axis=1)
        rows_of_2D_cells.append(cells_of_2D_cells)
    rows_of_2D_cells = np.concatenate(rows_of_2D_cells, axis=0)

    #print type(rows_of_2D_cells)
    #print rows_of_2D_cells.shape
    
    #print type(rows_of_2D_cells[0])
    #print rows_of_2D_cells[0].shape
    
    #print type(rows_of_2D_cells[0][0])
    #print rows_of_2D_cells[0][0].shape
    

    #for r in rows_of_2D_cells:
        #print r
        #print type(r)
        #print r.shape
        #for e in r:
            #print type(e)

    
    
    #return array_extract_2D
    return rows_of_2D_cells




def slice_cube(MAT, width, height, ppm):
    """NotImplemented"""
    NotImplemented





def test_mesh4():
    x = np.arange(0, 10, 1)
    y = np.arange(0, 10, 1)
    
    rows_of_2D_cells = []
    for i in range(len(x)):
        cells_of_2D_cells = []
        for j in range(len(y)):
            cells_of_2D_cells.append( (x[i], y[j]) )
        rows_of_2D_cells.append(cells_of_2D_cells)

    for r in rows_of_2D_cells:
        print r
        

def test_mesh3():
    @np.vectorize
    def t(x,y):
        a = (x,y)
        return a
    
    x = np.arange(0, 10, 1)
    y = np.arange(0, 10, 1)
    xx, yy = np.meshgrid(x, y, sparse=True)
    #z = t(xx,yy)
    #print z
    #print z.shape

    z = np.zeros( (len(x), len(y)), dtype=(int,2) )

    rows_of_2D_cells = []
    for i in range(len(x)):
        cells_of_2D_cells = []
        for j in range(len(y)):
            #print j, y[j]
            #z[i][j] = (x[i], y[j])
            cells_of_2D_cells.append( (x[i], y[j]) )
        rows_of_2D_cells.append(cells_of_2D_cells)
    print z.shape
    for r in rows_of_2D_cells:
        print r

def test_mesh2():
    @np.vectorize
    def t(x,y):
        a = (x,y)
        return a
    
    x = np.arange(0, 10, 1)
    y = np.arange(0, 10, 1)
    xx, yy = np.meshgrid(x, y, sparse=True)
    #z = t(xx,yy)
    #print z
    #print z.shape

    z = np.zeros( (len(x), len(y)), dtype=(int,2) )

    for i in range(len(x)):
        #print i, x[i]
        for j in range(len(y)):
            #print j, y[j]
            z[i][j] = (x[i], y[j])
    print z


def test_mesh():
    x = np.arange(0, 10, 1)
    y = np.arange(0, 10, 1)
    xx, yy = np.meshgrid(x, y, sparse=True)
    print xx.shape
    print xx
    print yy.shape
    print yy
    z = xx+yy
    print z
