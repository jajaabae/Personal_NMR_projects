

class ManualDataClass():
    CH_pairs = {}
    Hydrogens = {}
    Carbons = {}
    
    class CH_Pair():
        def __init__(self, definition_line_list, data_line_list):
            self.data = {}
            self.hasH = False
            self.hasC = False
            self.name = None
            self.export_strings = {}
            
            self.add_data(definition_line_list, data_line_list)
            ManualDataClass.CH_pairs[self.name]=self
            if self.hasH:
                ManualDataClass.Hydrogens[self.data['H-Name']]=self
            if self.hasC:
                ManualDataClass.Carbons[self.data['C-Name']]=self
            self.make_multiplicity_string()
            self.make_number_of_hydrogens()
            self.make_HSQC_pos_neg()            
            
        def add_data(self, definition_line_list, data_line_list):
            for a, x in zip(definition_line_list, data_line_list):
                self.data[a] = x
            if self.data['H-Name']:
                self.hasH = True
            if self.data['C-Name']:
                self.hasC = True

            if self.hasC:
                self.name = self.data['C-Name'][1:]
            else:
                self.name = self.data['H-Name'][1:]

        def print_export_strings(self):
            print self.name, ' -- ',
            for e in self.export_strings:
                if self.export_strings[e]:
                    print e+':', self.export_strings[e]+';', #self.export_strings
            print 

        def make_multiplicity_string(self):
            mult_str = ''
            if self.data['broadness']:
                mult_str += self.data['broadness']+' '
            if self.data['Multiplicity']:
                mult_str += self.data['Multiplicity']
            if self.data['J']:
                mult_str += ' ('+self.data['J']+')'
            self.export_strings['mult_str'] = mult_str
            
        def make_number_of_hydrogens(self):
            number_of_hydrogens = ''
            if self.data['Number of H']:
                number_of_hydrogens += self.data['Number of H']
            self.export_strings['number_of_hydrogens']=number_of_hydrogens

        def make_HSQC_pos_neg(self):
            HSQC_pos_neg = ''
            if self.data['pos/neg']:
                HSQC_pos_neg = self.data['pos/neg']
                #print 'ok'
            self.export_strings['HSQC_pos_neg'] = HSQC_pos_neg
            
    def __init__(self, the_file):
        self.manual_data = self.readDataFromFile(the_file)
        
    def readDataFromFile(self, the_file):
        definition_lines = the_file.readline().replace("\n", '').split(";")
        data_lines = [line.rstrip('\n') for line in the_file]

        CH_pairs = self.CH_pairs
        
        for l in data_lines:
            l=l.replace("\n", '').split(";")
            element = self.CH_Pair(definition_lines, l) #make CH-pair

    #def get_export_strings_dict(self):
        #for e in self.CH_Pair, Carbons and Hydrogens:
        #    ...
        #   return "e".export_strings



        
if __name__ == '__main__':
    import import_manual_data_table
    reload(import_manual_data_table)
    from import_manual_data_table import main_fun
    main_fun()
