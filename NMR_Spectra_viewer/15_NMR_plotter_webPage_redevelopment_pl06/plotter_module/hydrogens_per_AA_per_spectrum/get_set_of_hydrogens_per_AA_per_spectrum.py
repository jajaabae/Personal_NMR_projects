"""
Use "get_set_of_hydrogens_per_AA_per_spectrum" (others are local)
"""
def get_set_of_hydrogens_per_AA_per_spectrum(instructions):
    """
    OK
    """
    def init_dict_with_dict(d, e):
        if e not in d:
            d[e]={}
    
    sets_of_hydrogens = {}
    for aa in instructions['AA']:
        #print aa
        for spectrum in instructions['Spectra']:
            #print spectrum
            init_dict_with_dict(sets_of_hydrogens, aa)
            #sets_of_hydrogens[aa][spectrum] = aa+'-'+spectrum+' hydrogens'
            sets_of_hydrogens[aa][spectrum] = get_hydrogens_for_aa_with_spectrum(aa, spectrum)
    #print sets_of_hydrogens
    return sets_of_hydrogens



def get_hydrogens_for_aa_with_spectrum(aa, spectrum):
    """
    tmp_ok
    needs:
    - more spectrum types
    """
    #set_of_H = []
    if spectrum == 'ROESY':
        return get_H_for_ROESY(aa)
    return None


def get_H_for_ROESY(aa):
    """
    tmp_ok
    needs:
    - get atom_data or aa_spin_systems
    - get correlation_data
    """
    NotImplemented
    ### tmp:
    tmp_native  = [4.13,8.83,1.97,1.3,1.37,1.3,3.01,7.37,]
    tmp_correlated  = [1.30, 1.37, 1.97, 2.31, 7.14, 7.75, 8.83, 0.89, 1.30, 1.37, 3.12, 4.13, 6.09, 7.75, 3.01, 4.13, 7.37, 4.13, 8.83, 3.01, 4.13, 8.83, 3.01, 8.83, 1.30, 1.37, 1.97, 7.19, 7.27, 7.37, 1.97, 3.01, 3.12, ]
    tmp_correlated = list(set(tmp_correlated))
    Arg_tmp_ROESY_hydrogens = {'native':tmp_native, 'correlated':tmp_correlated}
    return Arg_tmp_ROESY_hydrogens
