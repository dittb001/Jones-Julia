#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:57:59 2020

@author: julia
"""

def load_constants(constantsfile):
    constants = {}

    infile = open(constantsfile, 'r')
    lines = infile.readlines()[2:]
    for line in lines:
        title = line[:27].strip() # Equilvalent to cutting to clipboard; column 1 turns into column 0
        value = float(line[27:].split()[0])
        constants[title] = value
    infile.close()
    return constants

fundamental_constants = load_constants('constants.txt')
print ('------------------------------------')
for constant, value in fundamental_constants.items():
    print ('{} {}'.format(constant, value))
print ('------------------------------------')

"""
Sample run:
python fundamental_constants.py
------------------------------------
Planck constant          6.62608e-34
elementary charge        1.60218e-19
speed of light           2.99792e+08
electron mass            9.10939e-31
Avogadro number          6.02214e+23
proton mass              1.67262e-27
gravitational constant   6.67259e-11
Boltzmann constant       1.38066e-23
------------------------------------
"""