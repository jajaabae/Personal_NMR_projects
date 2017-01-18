import numpy as np
import matplotlib.pyplot as plt
import nmrglue as ng

"""
def tmp_get_data(src):
    #src = 'Bruker_NMR_spectra/23/pdata/1'
    dic, data = ng.bruker.read_pdata(src)
    return dic, data
#"""

"""
#def tmp_plot_data(dic, data):
def tmp_plot_data(data):
    cl = data.std() * 1.6 * 0.73 ** np.arange(10)
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

    plt.register_cmap(name='test5', data=cdict5)  # optional lut kwarg
    ax.contour(data, cl, cmap=plt.get_cmap('test5'))

    fig.savefig('roesy_2d.png')
#"""

def tmp_get_stuff(dic, data):
    #print dic
    #print 'SF', dic['SF']

    #for e in dic:
    #    print e

    for e in dic['procs']:
        print e, dic['proc2s'][e]
    print ''

    print len(dic['proc2s'])
    print len(dic['procs'])

    print dic['procs']['SF']
    print dic['procs']['OFFSET']
    print dic['procs']['SW_p']

    print 'SW*', dic['procs']['SW_p'] / dic['procs']['SF']
    #print dic['procs']




if __name__ == '__main__':
    NotImplemented
    #dic, data = tmp_get_data()
    #tmp_get_stuff(dic, data)
    #tmp_plot_data(dic, data)







