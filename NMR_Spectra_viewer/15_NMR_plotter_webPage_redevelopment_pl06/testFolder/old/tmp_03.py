import re
list_string = '234,  65 34 43,3.1'
a_list = re.split('[ ,]', list_string)
b_list = filter(None, a_list)
print b_list


