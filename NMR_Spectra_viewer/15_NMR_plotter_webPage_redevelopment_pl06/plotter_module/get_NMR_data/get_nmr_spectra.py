import plotter_module.data_containers.SpectrumObjects
reload(plotter_module.data_containers.SpectrumObjects)
from plotter_module.data_containers.SpectrumObjects import SpectrumObject_2D

def get_nmr_spectra(spectra_type_list):
    """
    ok
    """
    spectra_objects = {}
    for spec_type in spectra_type_list:
        spectra_objects[spec_type] = SpectrumObject_2D(spec_type)
    return spectra_objects


        

