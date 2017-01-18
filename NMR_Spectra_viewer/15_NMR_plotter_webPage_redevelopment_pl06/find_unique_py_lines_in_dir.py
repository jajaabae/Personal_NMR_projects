import os

class find_unique_py_lines_in_dir():
    def __init__(s):
        s.unique_lines = set([])
        
    def add_list_of_lines(s, a_list):
        #s.unique_lines.add(set(a_list))
        s.unique_lines |= set(a_list)
        
    def get_unique_lines(s):
        return s.unique_lines

    def do_action_test(s, file_in_path):
        test=False
        if file_in_path[-3:] == '.py':
            test=True
        return test

    def action_per_file(s, file_in_path, depth):
        if s.do_action_test(file_in_path):
            lines = lines_of_file(file_in_path)
            s.add_list_of_lines(lines)

    def dig_dir(s, path, depth=0):
        for item in os.listdir(path):
            item_in_path = os.path.join(path,item)
            if os.path.isfile(item_in_path):
                #print item_in_path
                s.action_per_file(item_in_path, depth)
            else:
                #print 'FOLDER', item_in_path
                s.dig_dir(item_in_path, depth=depth+1)


def lines_of_file(file_in_path):
    f = open(file_in_path,'r')
    lines = f.readlines()
    f.close()
    return lines

def write_result_to_file(N_lines):
    f = open('result_unique_lines_is_'+str(N_lines)+'_.txt', 'w')
    output = "number of unique lines: {}".format(N_lines)
    f.write(output)
    f.close()


if __name__ == '__main__':
    ob = find_unique_py_lines_in_dir()
    
    path = os.getcwd()

    ob.dig_dir(path)
    
    unique_lines = ob.get_unique_lines()

    write_result_to_file(len(unique_lines))


    print 'len(unique_lines)', len(unique_lines)
    print
    #for l in unique_lines:
    #    print l.replace('\n','')
    print
    print 'len(unique_lines)', len(unique_lines)
        
