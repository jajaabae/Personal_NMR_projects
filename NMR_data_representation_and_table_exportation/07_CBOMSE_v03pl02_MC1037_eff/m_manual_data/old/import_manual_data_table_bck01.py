def import_manual_data_table(the_file):
    manual_data = None
    readDataFromFile(the_file)
    return manual_data

def readDataFromFile(the_file):
    print the_file.readline().replace("\n", '').split(";")
    print the_file.readlines()

def test():
    la = 'inactive;Amino Acid;Atom name;C-Name;pos/neg;H-Name;broadness;Multiplicity;J;Number of H'
    la = la.replace("\n", '').split(";")
    lx = ';;;;;HAdda5 3-NH;br;d;?;1'
    lx = lx.replace("\n", '').split(";")

    data_struc = {}
    data_struc['Hydrogens'] = {}
    data_struc['Carbons'] = {}
    data_struc['CH_pair'] = {}
    #for each line
    element = {}
    for a, x in zip(la, lx):
        print a, '--', x
        if x:
            element[a] = x
        else:
            element[a] = None
    if element['H-Name']:
        element['Has H']=True
    else:
        element['Has H']=False
    if element['C-Name']:
        element['Has C']=True
    else:
        element['Has C']=False
    #print '\nelement: ', element
    #end: for each line
    
    if element['Has H']:
        data_struc['Hydrogens'][element['H-Name']]=element
    if element['Has C']:
        data_struc['Carbons'][element['C-Name']]=element
    data_struc['CH_pair'][element['C-Name']]=element
    
    #data_struc['HAdda5 3-NH']={}
    print 
    print data_struc

def print_imported_manual_data(manual_data):
    print manual_data
    NotImplemented

if __name__ == '__main__':
    #the_file = open("manual_data_table.csv", 'r')
    #manual_data = import_manual_data_table(the_file)
    #the_file.close()
    #print_imported_manual_data(manual_data)

    test()
    
    
