#!/usr/bin/python
#*********************************************************************************
# nwvActiveSite.py
# May 17, 2014
# Bradley Kearney
# Returns 10 closest amino acids to the cleavage site of NWV.
#*********************************************************************************

from math import *
import sys
import os
from pdb import *
import numpy as np

def shell(cmd):
    return -1
   
class Analyzer:
    def __init__(self, pdb_filenames, root, err=1):
        self.pdbs = []
        totalnum = 0
        for filename in pdb_filenames:
            self.pdbs.append(PDB(filename, root + filename.split('/')[-1]))
        self.pdbs.sort(key=str)
        for i, pdb in enumerate(self.pdbs):
            pdb.number = i
            pdb.shortname = pdb.filename.split('/')[-1]
            totalnum = i
            
    def main(self):
        distances={}
        distances2={}
        self.createlist()
        for atom in self.aa:
            if atom['atom name']=="CA":
                #dist=atom.distance_from([5.094,  73.214, 147.441], ) #CAPSID A SUBUNIT
                #dist=atom.distance_from([51.636,  54.253, 129.844], )#CAPSID B SUBUNIT
                #dist=atom.distance_from([12.772,  20.911, 144.552], )#CAPSID C SUBUNIT
                #dist=atom.distance_from([60.340,  28.662, 126.650], )#CAPSID D SUBUNIT
                #procapsid below
                #dist=atom.distance_from([7.059,  78.752, 161.103], )#CAPSID A SUBUNIT
                #dist=atom.distance_from([65.297,  59.283, 151.133], )#CAPSID B SUBUNIT
                #dist=atom.distance_from([18.757,  19.609, 172.332 ], )#CAPSID C SUBUNIT
                #dist=atom.distance_from([74.295,  33.278, 154.523], )#CAPSID D SUBUNIT
                if dist<50:
                    if atom['res num']!=570:#Make sure it's not the active site residue itself...
                        distances2[dist]=atom.line
                    else:
                        distances[dist]=atom.line
        counter=0
        for key in sorted(distances.iterkeys()):
            print "%.2f: %s" % (key, distances[key])
            counter=counter+1
            if counter==10:
                print "======="
                break
        counter=0
        for key in sorted(distances2.iterkeys()):
            print "%.2f: %s" % (key, distances2[key])
            counter=counter+1
            if counter==10:
                break
    
def run():
    print "Preprocessing files. Please wait."
    argv = sys.argv[1:]
    def getArg(c, default):
        try:
            i = argv.index('-' + c)
            argv.pop(i)
            return argv.pop(i)
        except:
            return default
    root = getArg('r', 'Renumbered/')
    if(root[-1:] != '/'):
        root += '/'
    start_err = float(getArg('e', '1.0'))
    pdb_filenames = []
    if(argv):
        pdb_filenames = argv
    else:
        filenames = os.listdir(os.getcwd())
        for f in filenames:
            if(f[-4:] == '.pdb'):
                pdb_filenames.append(f)
    a = Analyzer(pdb_filenames, root, err=start_err)
    input = ''
    a.main()
    return
if(__name__ == '__main__'):
    run()
        
        
