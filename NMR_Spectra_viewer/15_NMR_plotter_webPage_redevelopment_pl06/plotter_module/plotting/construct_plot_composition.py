#import matplotlib.pyplot as plt




def construct_plot_composition(plt, size_x_and_y, height_1D_horiz, height_labels_horiz, height_1D_verti, height_labels_verti):
    #size_x_and_y = 20*2
    #x,y = size_x_and_y,size_x_and_y
    x,y = size_x_and_y
    
    ax0 = None
#    height_1D = height_1D_horiz
    #height_labels = height_labels_horiz
    #ax0 = plt.subplot2grid((x, y), (0, 0))
    top = plt.subplot2grid((x, y), (0, height_1D_verti), colspan=x-height_1D_verti-height_labels_verti, rowspan=height_1D_horiz)
    left = plt.subplot2grid((x, y), (height_1D_horiz, 0), colspan=height_1D_verti, rowspan=y-height_1D_horiz-height_labels_horiz)
    
    bot = plt.subplot2grid((x, y), (y-height_labels_horiz, height_1D_verti), colspan=x-height_1D_verti-height_labels_verti, rowspan=height_labels_horiz)
    right = plt.subplot2grid((x, y), (height_1D_horiz, x-height_labels_verti), colspan=height_labels_verti, rowspan=y-height_1D_horiz-height_labels_horiz)
    #height_1D = height_1D_horiz
    #bot.get_yaxis().set_visible(False)
    bot.get_xaxis().set_visible(False)
    bot.yaxis.set_ticks_position('none')
    bot.yaxis.set_ticks([], [])
    #right.get_xaxis().set_visible(False)
    right.get_yaxis().set_visible(False)
    #right.yaxis.set_ticks_position('right')
    #right.yaxis.set_ticks_position('none')
    right.xaxis.set_ticks([], [])


    #ax0.get_xaxis().set_visible(False)
    #ax0.get_yaxis().set_visible(False)

    top.get_xaxis().set_visible(False)
    top.get_yaxis().set_visible(False)
    top.xaxis.set_ticks_position('top')

    left.get_xaxis().set_visible(False)
    left.get_yaxis().set_visible(False)
    
    main = plt.subplot2grid((x, y), (height_1D_horiz, height_1D_verti), colspan=x-height_1D_verti-height_labels_verti, rowspan=y-height_1D_horiz-height_labels_horiz)
    #main.get_xaxis().set_visible(False)
    #main.get_yaxis().set_visible(False)
    main.yaxis.set_ticks_position('right')

    #plt.rc('grid', linestyle="-", color='black')
    #plt.grid(True)

    #ax0.plot([1, 2])
    #main.plot([1,2,3,5,7,54,3,5,67,7,42,4,6,7,8,9,43,5,43,])

    return ax0, top, left, main, right, bot








def main_for_testing():
    fig = plt.figure()
    ax0, top, left, main = construct_plot_composition(plt)
    ax0.plot([1, 2])
    main.plot([1,2,3,5,7,54,3,5,67,7,42,4,6,7,8,9,43,5,43,])
    plt.savefig('out09.png')






if __name__ == '__main__':
    main_for_testing()















###################################################################
### OLD ###########################################################
###################################################################
def edited():
    fig = plt.figure()
    x,y = 6,6
    ax0 = plt.subplot2grid((x, y), (0, 0))
    top = plt.subplot2grid((x, y), (0, 1), colspan=x, rowspan=1)
    left = plt.subplot2grid((x, y), (1, 0), colspan=1, rowspan=y)
    main = plt.subplot2grid((x, y), (1, 1), colspan=x, rowspan=y)

    ax0.get_xaxis().set_visible(False)
    ax0.get_yaxis().set_visible(False)

    #top.get_xaxis().set_visible(False)
    top.get_yaxis().set_visible(False)
    top.xaxis.set_ticks_position('top')

    left.get_xaxis().set_visible(False)
    #left.get_yaxis().set_visible(False)

    #main.get_xaxis().set_visible(False)
    #main.get_yaxis().set_visible(False)
    main.yaxis.set_ticks_position('right')

    plt.rc('grid', linestyle="-", color='black')
    
    plt.grid(True)

    ax0.plot([1, 2])
    main.plot([1,2,3,5,7,54,3,5,67,7,42,4,6,7,8,9,43,5,43,])
    #main.plot([[1,2,3],[5,3,2]] )

    plt.plot([0, 1], [0, 3], '-k')

    plt.axhline(4, color='red')
    plt.axvline(4, color='red')
    
    plt.savefig('out08.png')

#edited()
    
###################################################################
###################################################################
