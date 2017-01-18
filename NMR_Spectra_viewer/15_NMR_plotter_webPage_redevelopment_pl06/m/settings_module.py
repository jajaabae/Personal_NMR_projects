

def read_settings(settings_file):
    f = open(settings_file, 'r')
    settings_lines = f.readlines()
    f.close()

    settings_dict = {}
    
    for l in settings_lines:
        #print l
        l = l.replace('\n','')
        if len(l)>0:
            settings_dict[l.split('\t')[0]] = l.split('\t')[1]

    #print settings_dict
    return settings_dict


def write_changed_settings():
    NotImplemented


def get_settings_from_file():
    settings_file = 'settings.txt'
    return read_settings(settings_file)


def test(settings_file):
    print read_settings(settings_file)


if __name__ == '__main__':
    settings_file = 'settings.txt'
    test(settings_file)
