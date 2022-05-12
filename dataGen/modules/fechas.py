#!/usr/bin/env python3
# Encoding: UTF-8
# By: Jorge L. Herrera 


from datetime import datetime
from random import randint as rint 


def headOut(i):
    h = "\n====  ====  ===="
    l = ['Dias', 'Meses', 'Años']
    print(h)
    if i == 1:
        for i in l: 
            print(i, end='  ')
        

    if i == 2:
        for i in l[::-1]: 
            print(i, end='  ')
        

    if i == 3:
        l[2], l[0] = l[0], l[2]
        for i in l: 
            print(i, end='  ')
    
    return '' 


class genDate:
    # al crear una instancia no se enviaran ningun arg
    def __init__(self):
        pass

    def dateGen(self, dateIni, cantidad, fmt, save):

        save        = False if save == None else True 
        s           = '/'
        d, m, y     = [int(_) for _ in dateIni.split(':')]  # dateIni.split(':') genera un list y los separa por el char :
        dt_year		= datetime.now().year
        dt_month 	= datetime.now().month
        dt_day		= datetime.now().day

        arr = [[str(rint(d, dt_day)), str(rint(m, dt_month)), str(rint(y, dt_year))] for _ in range(int(cantidad))]

        if fmt == 'A' or fmt == 'a':
            if save:
                return arr

            else:
                print(headOut(1))
                for n in arr:
                    print(n[0] + s + n[1] + s + n[2])
                return ''

        elif fmt == 'B' or fmt == 'b':
            if save:
                return arr
        
            else:
                print(headOut(2))
                for n in arr:
                    print(n[1] + s + n[0] + s + n[2])
                return arr

        elif fmt == 'C' or fmt == 'c':
            if save:
                return arr
                
            else:
                print(headOut(3))
                for n in arr:
                    print(n[2] + s + n[1] + s + n[0])
                return arr
        