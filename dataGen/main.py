#!/usr/bin/env python3
# Encoding: UTF-8
# By: Jorge L. Herrera


import logging
import argparse
import os
import time
from datetime import datetime
from modules.banr import bn
from modules.numers import genNum
from modules.nombres import genName
from modules.fechas import genDate
from modules.email import genEmail
from modules.clr import c

logging.basicConfig(
    level       = logging.DEBUG,
    filename    = 'logfile.log',
    filemode    = 'a',
    format      = '[ %(asctime)s ] | [ %(levelname)s ] | [ %(name)s ] | %(message)s'
)

with open('logfile.log', 'rt+') as f:
    cont = f.read()
    if cont == '':
        f.write("\t\t\t\t::: Log file created succesfully :::\n")

logging.info('Iniciando D. Gen')

parser = argparse.ArgumentParser()

# parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
#                         description=f"{module_name} (Version {__version__})"
#                        )

parser.add_argument('-i', '--interactive', help='Modo interactivo [y|n]', type=str, required=False) # or required=True
parser.add_argument('-e', '--email', help='Generar lista especificar cantidad en numeros', type=int, required=False) # or required=True
parser.add_argument('-d', '--date', help='Generar lista especificar cantidad en numeros', type=int, required=False) # or required=True
parser.add_argument('-n', '--name', help='Generar lista especificar cantidad en numeros', type=int, required=False) # or required=True
parser.add_argument('-u', '--number', help='Generar lista especificar cantidad en numeros', type=int, required=False) # or required=True
parser.add_argument('-p', '--phone', help='Generar lista especificar cantidad en numeros', type=int, required=False) # or required=True
args = parser.parse_args()



def interactiv():
    info = lambda s: print(
        s,
        """Este Script fue creado con fines educativos 
        no con la intencion de utilizar los datos para fines ilicitos uselo con responsabilidad"""
    )
    logging.info("Entrada en modo interactivo")
    opts = f"""
    +---------------------------+
    | {c.yellow}Ingresa la opcion deseada{c.fin} +
    +---------------------------+
    {c.cyan}| 1 | Generar fechas 
    | 2 | Generar Email's
    | 3 | Generar nombres
    | 4 | Generar DNI's
    | 5 | Generar Celulares
    | 6 | Info
    | 7 | Salir{c.fin}
    +---------------------------+
    """
    while True:
        print(opts)
        op = input('< D.GEN >')
        if op is '1':
            obj = genDate()
            i = input('cantidad:')
            fmt = input("format:")
            inicio = input('inicio (SEPARADO POR : ej. 02:03:1998 ):')
            if inicio == '':
                inicio = '12:12:2010'
            obj.dateGen(inicio, i, fmt, None)
            
        if op is '2':
            obj = genEmail()
            ca = int(input('Cantidad:'))
            m = input('| a | Mayusc\n| b | Minusc\n:')
            l = input('Email largo? si o no:')
            
            obj.gEmail(ca, m, l, None)
        if op is '3':
            obj = genName()
            gn = int(input('Cantidad:'))
            formt = input('| A | Nombres y apellidos  \n| b |  Apellidos y nombres')
            obj.geName(gn, formt, False)

        if op is '4':
            nu = int(input('Cantidad:'))
            obj = genNum('dni')
            obj.dninum(nu)

        if op is '5':
            ph = int(input('Cantidad:'))
            obj = genNum('phone')
            obj.celnum(ph)

        if op is '6':
            dtNow = '/'.join([str(datetime.now().year), 
                            str(datetime.now().month), 
                            str(datetime.now().day)])
            obj = info(dtNow)

        if op is '7':
            logging.info('Programa finalizando')
            print('[*] log file updated logfile.log')
            time.sleep(.2)
            exit()
        time.sleep(5)

if args.interactive:
    interactiv()
