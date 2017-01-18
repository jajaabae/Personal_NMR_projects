import ManualDataClass
reload(ManualDataClass)
from ManualDataClass import ManualDataClass

def import_manual_data_table(the_file):
    NotImplemented
    
def print_imported_manual_data(manual_data):
    NotImplemented
    
def main_fun():
    the_file = open("manual_data_table.csv", 'r')
    #manual_data = import_manual_data_table(the_file)
    mdc = ManualDataClass(the_file)
    the_file.close()
    #print_imported_manual_data(manual_data)
    
    print len(mdc.CH_pairs)
    print 
    for pair_name in mdc.CH_pairs:
        #print mdc.CH_pairs[pair_name].export_strings
        mdc.CH_pairs[pair_name].print_export_strings()
        #print mdc.CH_pairs[pair_name].tmp



if __name__ == '__main__':
    main_fun()
    
    #test()
    
    
