import re
list_string = '234,65'
list_string = '234,  65 34 43,3.1'

#print list_string.split(',')

#print [float(e) for e in list_string.split(',')]


print re.split('\W+', list_string)

print re.split('[ ,]', list_string)

a_list = re.split('[ ,]', list_string)
#a_list.remove('')
#print a_list

b_list = filter(None, a_list)
print b_list


