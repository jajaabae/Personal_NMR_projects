
list_string = '234,65'
list_string = '234,  65'

print list_string.split(',')

print [float(e) for e in list_string.split(',')]
