import os

def mfi():
    pass

def fi(fn):
    s = '''
global %s
from m.%s import %s
'''
    s = s%(fn, fn, fn)
    return s


def rfi(fn):
    s = '''
global %s
import m.%s
reload(m.%s)
from m.%s import %s
'''
    s = s%(fn, fn, fn, fn, fn)
    return s

def fi_fsf(folder, fn):
    s = '''
global %s
from %s.%s import %s
'''
    s = s%(fn, folder, fn, fn)
    #print s
    return s

def makeInitIfNeeded(folder):
    fip = '/'.join([folder, '__init__.py'])
    if not os.path.isfile(fip):
        f = open(fip, 'w')
        f.close()

def imp():
    s ='''
import os
from m.mfi import fi
def i(fn): #import
    exec(fi(fn))

from m.mfi import rfi    
def rni(fn): #reload and import
    exec(rfi(fn))

def ifl(aList): #import from list
    for fn in aList:
        i(fn)

from m.mfi import fi_fsf
def i_fsf(folder_and_fn): #import
    [folder, fn] = folder_and_fn.split('.')
    makeInitIfNeeded(folder)
    exec(fi_fsf(folder, fn))
    
def iaff(folder): #import all from folder
    for item in os.listdir(folder):
        fip = '/'.join([folder, item])
        if os.path.isfile(fip) and item[-3:] =='.py':
            i_fsf(folder+'.'+item[0:-3] )

from m.mfi import makeInitIfNeeded

'''
    return s


