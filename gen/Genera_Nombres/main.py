#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Created by Jorge L. Herrera

__autor__ 	= 'Jorge L. Herrera'
__version__ = '0.1'
__gmail__ 	= 'jorgeherreraluis972@gmail.com'


import random
import os
import argparse


from src.color import C
from src.adding import NA, AP, SP


HELPI  	= f'|---> {C.Y}[!]{C.B} Formato de salidad [A] Nombres y Apellidos, [B] Apellidos Nombres{C.E}'
ERR 	= ':('
temp 	= []
ERR_O 	= False
hide 	= False
saving_to = f'|---> {C.Y}[!]{C.B} Saving to file.txt yes | not [ y=si | n=no ] {C.E}'
parser 	= argparse.ArgumentParser()
parser.add_argument('-i', '--interactive', help='Modo interactivo [ y=si | n=no ]', type=str, required=False) # or required=True
parser.add_argument('-c', '--names', help='Cantidad de nombres [Numbers]', type=int, required=False)
parser.add_argument('-f', '--format', help=HELPI, type=str, required=False)
parser.add_argument('-s', '--save', help=saving_to, type=str, required=False)
args 	= parser.parse_args()


def banner():

    # Cleaner
    if os.sys.platform == 'win32':
        os.system('cls')

    else:
        os.system('clear')

    bn = f"""{C.G}
        _________________________________________________
        ----__----__----__---------__----__---_--_----__-
          /   ) /___) /   )      /   )  ___) / /  ) /___)
        _(___/_(___ _/___/______/___/_(___(_/_/__/_(___ _
            /             ------                         
        (_ / {C.P} version: {__version__}\n\t\t      Created by:{__autor__}{C.E}\n"""


    BNR = f'''
|---> {C.R}[*]{C.B} WELCOME{C.E}'''
    print(bn, BNR)
    return None


def trouble(c, f, x):
    # de acuerdo al parametro pasado a esta funcion
    ini = 0

    if not x:

        if f == 'a' or f == 'A':
            for _ in range(c):
                temp.append(' '.join([random.choice(NA), random.choice(AP), random.choice(SP)]))
                print(temp[ini])
                ini += 1

        if f == 'b' or f == 'B':	
            for _ in range(c):
                temp.append(' '.join([random.choice(AP), random.choice(SP), random.choice(NA)]))
                print(temp[ini])
                ini += 1

    if x:

        if f == 'a' or f == 'A':
            for _ in range(c):
                temp.append(' '.join([random.choice(NA), random.choice(AP), random.choice(SP)]))
                ini += 1

        if f == 'b' or f == 'B':	
            for _ in range(c):
                temp.append(' '.join([random.choice(AP), random.choice(SP), random.choice(NA)]))
                ini += 1
        


def saving_file():
    # Save

    m 		  = 0
    extencion = '.txt'
    gene_num  = random.randint(0, 50)
    name_file = 'file_'
    file_name = ''.join(['.\\', name_file, str(gene_num), extencion])

    with open(file_name, 'w') as fi:
        for _ in temp:
            fi.write(str(temp[m]))
            fi.write('\n')
            m += 1

    if os.path.exists(file_name):

        print(f'|---> {C.Y}[!]{C.B} Completed saved...{C.E}')

    else:
        print(ERR)

def ev():

    print(f'|---> {C.R}[+]{C.B} Inicializing...{C.E}')

    if args.interactive:
        
        cantidad = int(input(f'|---> {C.R}[+]{C.B} Cantidad de nombres: {C.E}'))
        print(HELPI)
        formato = str(input(f'|---> {C.R}[+]{C.B} Formato de salida [A] | [B]: {C.E}'))
        if formato == 'A' or formato == 'a':
            trouble(cantidad, formato, None)

        elif formato == 'B' or formato == 'b':
            trouble(cantidad, formato, None)

    if args.names:
        
        if args.names and not args.format:
            try:
                trouble(args.names, 'a', None)

            except:
                print(f'|---> {C.R}[x]{C.B} {ERR} La cantidad debe estar en numeros...{C.E}')

        if args.names and args.format:

            try:
                trouble(args.names, args.format, None)

            except:
                print(f'|---> {C.R}[x]{C.B} {ERR} La cantidad debe estar en numeros...{C.E}')

        if args.names and args.format and args.save:

            # Calling saving and not show
            hide = True
            trouble(args.names, args.format, hide)	
            saving_file()

        # cantidad = int(input(f'|---> {C.R}[+]{C.B} Cantidad de nombres: {C.E}'))
        # print(HELPI)
        # formato = str(input(f'|---> {C.R}[+]{C.B} Formato de salida [A] | [B]: {C.E}'))
        
        # trouble(cantidad, formato, hide)

if __name__ == "__main__":
    "Calling"

    if args.interactive or args.names or args.save:
        banner()
        ev()

    else:
        print(f'{C.R}[x]{C.R} {C.B}Not found parameters... type \'./main.py --help\' for more information...{C.E}')
