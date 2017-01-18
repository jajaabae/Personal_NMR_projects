def import_manual_data_table(the_file):
    manual_data = None
    manual_data = readDataFromFile(the_file)
    return manual_data


def readDataFromFile(the_file):
    definition_lines = the_file.readline().replace("\n", '').split(";")
    data_lines = [line.rstrip('\n') for line in the_file]

    data_struc = {}
    data_struc['Hydrogens'] = {}
    data_struc['Carbons'] = {}
    data_struc['CH_pair'] = {}
    
    for l in data_lines:
        element = {}
        l=l.replace("\n", '').split(";")
        for a, x in zip(definition_lines, l):
            element[a] = x

        if element['H-Name']:
            data_struc['Hydrogens'][element['H-Name']]=element
        if element['C-Name']:
            data_struc['Carbons'][element['C-Name']]=element

        if element['C-Name']:
            #print element['C-Name'][1:]
            data_struc['CH_pair'][element['C-Name'][1:]]=element
        else:
            #print element['H-Name'][1:]
            data_struc['CH_pair'][element['H-Name'][1:]]=element
            
        
    return data_struc


def get_multiplicity_string_for_hydrogen(hydrogen_name, manual_data):
    H = manual_data['Hydrogens'][hydrogen_name]
    mult_str = ''
    if H['broadness']:
        mult_str += H['broadness']+' '
    if H['Multiplicity']:
        mult_str += H['Multiplicity']
    if H['J']:
        mult_str += ' ('+H['J']+')'
    return mult_str


def get_number_of_hydrogens(hydrogen_name, manual_data):
    H = manual_data['Hydrogens'][hydrogen_name]
    number_of_hydrogens = ''
    if H['Number of H']:
        number_of_hydrogens += H['Number of H']
    return number_of_hydrogens


def get_HSQC_pos_neg(carbon_name, manual_data):
    HSQC_pos_neg = ''
    C = manual_data['Carbons'][carbon_name]
    if C['pos/neg']:
        HSQC_pos_neg = C['pos/neg']
    return HSQC_pos_neg


def print_imported_manual_data(manual_data):
    NotImplemented
    """
    for hydrogen_name in manual_data['Hydrogens']:
        mult_str = get_multiplicity_string_for_hydrogen(hydrogen_name, manual_data)
        number_of_hydrogens = get_number_of_hydrogens(hydrogen_name, manual_data)
        out = ' -- '.join([mult_str, number_of_hydrogens ])
        if out:
            print hydrogen_name, '--', out
    #"""


#def add_print_strings_to_manual_data(manual_data):
    for CH_pair_name in manual_data['CH_pair']:
        #if CH_pair_name == 'Adda5':
        if manual_data['CH_pair'][CH_pair_name]['Amino Acid'] == 'Adda5':
            print CH_pair_name, manual_data['CH_pair'][CH_pair_name]['C-Name'], manual_data['CH_pair'][CH_pair_name]['H-Name']
            hydrogen_name = manual_data['CH_pair'][CH_pair_name]['H-Name']
            if hydrogen_name:
                mult_str = get_multiplicity_string_for_hydrogen(hydrogen_name, manual_data)
                number_of_hydrogens = get_number_of_hydrogens(hydrogen_name, manual_data)

                out_list = [mult_str, number_of_hydrogens ]
                out_test = ''.join(out_list) #check if there are any elements
                out = ' -- '.join(out_list)
                if out_test:
                    print hydrogen_name, '--', out
            carbon_name = manual_data['CH_pair'][CH_pair_name]['C-Name']
            if carbon_name:
                HSQC_pos_neg = get_HSQC_pos_neg(carbon_name, manual_data)
                if HSQC_pos_neg:
                    print HSQC_pos_neg
            print 



if __name__ == '__main__':
    the_file = open("manual_data_table.csv", 'r')
    manual_data = import_manual_data_table(the_file)
    the_file.close()
    print_imported_manual_data(manual_data)

    #test()
    
    
