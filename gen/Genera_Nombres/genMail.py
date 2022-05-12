#!/usr/bin/env python3
#-*- Coding:UTF-8 -*-
# Created by: Jorge Herrera


from src.adding import NA, AP, SP
from src.bnr import IMG
from src.color import C


import random
import argparse
import os
# import sys


# cleanScream
os.system('cls') if os.sys.platform == 'win32' else os.system('clean')
print(IMG)

TMP = []
CNT = 'Cantidad de GMAIL [Numbers]: '
HLP = 'MAYC=m|minusc=n: '

# parser
parser  = argparse.ArgumentParser()
parser.add_argument('-i', '--A',  help = 'Modo interactivo [ y=si | n=no ]', type=str, required=False) # or required=True
parser.add_argument('-c', '--B',  help = CNT, type=int, required=False)
parser.add_argument('-f', '--C',  help = HLP, type=str, required=False, default='n')
parser.add_argument('-s', '--D',  help = '<Save the file with list of gmails> [Y] | [N]', type=str, required=False)
args    = parser.parse_args() 

# if sys.argv[2] == '--help' or sys.argv[2] == '-h':
print("""\
    [NOTE] The -s argument don\'t required name 
    the file, the moment call the switch the 
    request name for file. for more information 
    write \'python .//main.py --help\'
    """
)

def gCreate(s = True):
    """ Genera gmails"""

    # add your extensions
    gend   =   [
                '@gmail.com',
                '@hotmail.com',
                '@net.com'
                ]
    if s:
        x  =   int(input(CNT))
        y  =   input(HLP)

    else:
        x  = args.B
        y  = args.C

    for _ in range(x):
        TMP.append(''.join([random.choice(NA), 
                    random.choice(AP), 
                    str(random.randint(1, 50)), 
                    random.choice(gend)])
    )

    # MAYUSC
    if y == 'm' or y == 'M':
        for i in TMP:
            # join(index of i to char @ after just show uppercase) 
            print(''.join([i[0:i.find('@')].upper(), i[i.find("@"):len(i)]]))

    # minuscula
    elif y == 'n' or y == 'N':
        for i in TMP:
             # join(index of i to char @ after just show lowercase)
            print(''.join([i[0:i.find('@')].lower(), i[i.find("@"):len(i)]]))

    else:
        for i in TMP:
            print(i)

def saveGen():
    """ this function save the list of the gmail's"""
    try:

        name = input('Nombre del archivo:')

    except:

        print('[X] Nombre invalido...')

    gCreate(False)

    with open(''.join([name, '.txt']), 'w') as f:

        for i in TMP:
            f.write(str(i))
            f.write('\n')

        print(f'{C.Y}[{f.name}]{C.B} Archivo Generado {C.E}')
        
    return ''

if args.A:

    if args.A == 'y' or args.A == 'Y':
        # interactive 
        gCreate(True)

else:
    if args.D == 'y' or args.D == 'Y':
        saveGen()
    else: 
        gCreate(False)



