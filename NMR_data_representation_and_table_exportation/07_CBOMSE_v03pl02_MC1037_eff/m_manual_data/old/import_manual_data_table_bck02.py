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
            #print a, '--', x
            element[a] = x
            #if x:
                #element[a] = x
            #else:
                #element[a] = None

        """
        if element['H-Name']:
            element['Has H']=True
        else:
            element['Has H']=False
        if element['C-Name']:
            element['Has C']=True
        else:
            element['Has C']=False
    
        if element['Has H']:
            data_struc['Hydrogens'][element['H-Name']]=element
        if element['Has C']:
            data_struc['Carbons'][element['C-Name']]=element
        data_struc['CH_pair'][element['C-Name']]=element
        #"""
        if element['H-Name']:
            data_struc['Hydrogens'][element['H-Name']]=element
        if element['C-Name']:
            data_struc['Carbons'][element['C-Name']]=element
        data_struc['CH_pair'][element['C-Name']]=element
        
    return data_struc

def get_multiplicity_string_for_hydrogen(hydrogen_name, manual_data):
    H = manual_data['Hydrogens'][hydrogen_name]
    print hydrogen_name, '(',H['broadness'], H['Multiplicity'], H['J'], H['Number of H'], ')'

def print_imported_manual_data(manual_data):
    NotImplemented
    #print manual_data
    #print manual_data['Hydrogens']
    for hydrogen_name in manual_data['Hydrogens']:
        #H = manual_data['Hydrogens'][hydrogen_name]
        get_multiplicity_string_for_hydrogen(hydrogen_name, manual_data)
        #print e, manual_data['Hydrogens'][e]
        #print e, '(',H['broadness'], H['Multiplicity'], H['J'], H['Number of H'], ')'
    


if __name__ == '__main__':
    the_file = open("manual_data_table.csv", 'r')
    manual_data = import_manual_data_table(the_file)
    the_file.close()
    print_imported_manual_data(manual_data)

    #test()
    
    
