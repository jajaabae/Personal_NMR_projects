import ManualDataClass
reload(ManualDataClass)
from ManualDataClass import ManualDataClass

def import_manual_data_table(the_file):
    mdc = ManualDataClass(the_file)
    return mdc
    
def print_imported_manual_data(mdc):
    print len(mdc.CH_pairs)
    print 
    for pair_name in mdc.CH_pairs:
        mdc.CH_pairs[pair_name].print_export_strings()

    
def main_fun():
    the_file = open("manual_data_table.csv", 'r')
    mdc = import_manual_data_table(the_file)
    the_file.close()
    print_imported_manual_data(mdc)
    ##export_strings_dict = mdc.get_export_strings_dict()
    ##print export_strings_dict
    #print mdc.Hydrogens['HAdda5 2'].data#['Amino Acid']


if __name__ == '__main__':
    main_fun()
    
    #test()
    
    
