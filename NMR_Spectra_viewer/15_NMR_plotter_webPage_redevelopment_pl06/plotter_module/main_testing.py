"""
"""

import hydrogens_per_AA_per_spectrum.get_set_of_hydrogens_per_AA_per_spectrum
from hydrogens_per_AA_per_spectrum.get_set_of_hydrogens_per_AA_per_spectrum import get_set_of_hydrogens_per_AA_per_spectrum #pck

import time

import tmp.tmp_07_
#reload(tmp.tmp_07_)
#from tmp.tmp_07_ import tmp_get_data
from tmp.tmp_07_ import tmp_get_stuff
#from tmp.tmp_07_ import tmp_plot_data

import data_containers.SpectrumObjects
#reload(data_containers.SpectrumObjects)
from data_containers.SpectrumObjects import SpectrumObject_2D

import plotting.plot_ROESY_spectrum
from plotting.plot_ROESY_spectrum import plot_ROESY_spectrum



def test01():
    instructions = {'AA': ['Arg4'],
                    'Spectra': ['ROESY'],
                    }
    sets_of_hydrogens = get_set_of_hydrogens_per_AA_per_spectrum(instructions)
    print 'sets_of_hydrogens:', sets_of_hydrogens

    get_nmr_spectra(instructions['Spectra'])
    get_nmr_data_for_spectrum_by_type()
    

def get_nmr_spectra(spectra_type_list):
    #print spectra_type_list
    spectra_objects = {}
    NotImplemented
    for spec_type in spectra_type_list:
        if spec_type == 'ROESY':
            spectra_objects['ROESY'] = get_nmr_data_for_spectrum_by_type(spec_type)
        

def get_nmr_data_for_spectrum_by_type():
    NotImplemented


import get_NMR_data.read_Bruker_2D
reload(get_NMR_data.read_Bruker_2D)
from get_NMR_data.read_Bruker_2D import read_Bruker_2D

def test_the_tmp07():
    src = 'Bruker_NMR_spectra/23/pdata/1'
    #attr_dic, spectrum_array = tmp_get_data(src)
    attr_dic, spectrum_array = read_Bruker_2D(src)
    

    a = SpectrumObject_2D(attr_dic, spectrum_array)
    print a
    print type(a.spectrum_array)
    
    #tmp_get_stuff(attr_dic, data)
    #tmp_plot_data(attr_dic, a.spectrum_array)
    #tmp_plot_data(a.spectrum_array)

    out_file_name = 'roesy_2d.png'
    plot_ROESY_spectrum(a.spectrum_array, out_file_name)




if __name__ == '__main__':
    #test01()
    test_the_tmp07()

    print 'Done.'
    time.sleep(1)




