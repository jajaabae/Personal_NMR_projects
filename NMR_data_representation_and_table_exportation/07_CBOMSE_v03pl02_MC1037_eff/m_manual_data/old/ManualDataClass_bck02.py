

class ManualDataClass():
    CH_pairs = {}
    
    class CH_Pair():
        data = {}
        hasH = False
        hasC = False
        name = None
        tmp = ''
        export_strings = None
        #export_strings = {}
        def __init__(self, definition_line_list, data_line_list):
            self.export_strings = {} # Needed to be initiated for some obscure reason.
            self.add_data(definition_line_list, data_line_list)
            ManualDataClass.CH_pairs[self.name]=self
            self.make_multiplicity_string()
            
            
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
            #print self.name

        def print_export_strings(self):
            print self.name, ' -- ',
            #print self.name, 'self.export_strings:', self.export_strings
            for e in self.export_strings:
                #print e, self.export_strings[e], '*', self.tmp, self.export_strings, self.export_strings['mult_str']
                print self.export_strings[e],
            print 

        def make_multiplicity_string(self):
            #H = manual_data['Hydrogens'][hydrogen_name]
            export_strings = self.export_strings
            mult_str = ''
            if self.data['broadness']:
                mult_str += self.data['broadness']+' '
            if self.data['Multiplicity']:
                mult_str += self.data['Multiplicity']
            if self.data['J']:
                mult_str += ' ('+self.data['J']+')'
            #print self.name,
            #self.export_strings['mult_str'] = mult_str
            export_strings['mult_str'] = mult_str
            #print export_strings
            self.export_strings = export_strings
            #print self.name, self.export_strings,
            #self.print_export_strings()
            self.tmp = mult_str
            
    def __init__(self, the_file):
        self.manual_data = self.readDataFromFile(the_file)
        
    def readDataFromFile(self, the_file):
        definition_lines = the_file.readline().replace("\n", '').split(";")
        data_lines = [line.rstrip('\n') for line in the_file]

        CH_pairs = self.CH_pairs
        
        for l in data_lines:
            l=l.replace("\n", '').split(";")
            element = self.CH_Pair(definition_lines, l) #make CH-pair



        
if __name__ == '__main__':
    import import_manual_data_table_branch02_classBased
    reload(import_manual_data_table_branch02_classBased)
    from import_manual_data_table_branch02_classBased import main_fun
    main_fun()
