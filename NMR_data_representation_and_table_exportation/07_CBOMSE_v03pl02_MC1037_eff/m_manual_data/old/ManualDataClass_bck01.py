

class ManualDataClass():
    data_struc = {}
    #data_struc['Hydrogens'] = {}
    #data_struc['Carbons'] = {}
    data_struc['CH_pair'] = {}

    #class Hydrogen():
    #    hydrogen_data = None
    #    Carbon = None
    #    def add_data():
    #        print '*'
    #class Carbon():
    #    carbon_data = None
    #    Hydrogen = None
    class CH_Pair():
        #pair_name = None
        #Carbon = None
        #Hydrogen = None
        data = {}
        def __init__(self):
        #    self.Hydrogen = Hydrogen()
        #    self.Carbon = Carbon()
            pass
            
        def add_data(self, definition_line_list, data_line_list):
            for a, x in zip(definition_line_list, data_line_list):
                self.data[a] = x
            
    def __init__(self, the_file):
        self.manual_data = self.readDataFromFile(the_file)
        
    def readDataFromFile(self, the_file):
        definition_lines = the_file.readline().replace("\n", '').split(";")
        data_lines = [line.rstrip('\n') for line in the_file]

        data_struc = self.data_struc
        #data_struc['Hydrogens'] = {}
        #data_struc['Carbons'] = {}
        #data_struc['CH_pair'] = {}
        #print data_struc
        
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
                
            
        self.data_struc = data_struc
            
        
if __name__ == '__main__':
    import import_manual_data_table_branch02_classBased
    reload(import_manual_data_table_branch02_classBased)
    from import_manual_data_table_branch02_classBased import main_fun
    main_fun()
