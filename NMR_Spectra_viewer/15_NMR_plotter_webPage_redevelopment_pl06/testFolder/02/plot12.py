import matplotlib.pyplot as plt




def construct_plot_composition(plt):
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

    #plt.rc('grid', linestyle="-", color='black')
    #plt.grid(True)

    #ax0.plot([1, 2])
    #main.plot([1,2,3,5,7,54,3,5,67,7,42,4,6,7,8,9,43,5,43,])

    return ax0, top, left, main








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
