#!/usr/bin/env python 3.7
#-*- coding: utf-8 -*-
# Genera fechas aleatorias 
# Created by: Jorge l. Herrera 

from datetime import datetime
from random import randint as rint
import argparse
import time
import os

usage = '| usage: f.py -h for help'
name  = '-- Generando fechas --'
slash = '/'
version = 0.1
list_alterned = []
one = '\\'
two = '\\'
inf = '\n| [*]Este script genera fechas de manera aleatoria y tambien puede almacenarlas en archivos csv o txt'

class color_con:
	"""console_colors"""
	CYAN   = '\033[96m'
	BLUE   = '\033[94m'
	RED    = '\033[91m'
	YELLOW = '\033[93m' 
	PURPLE = '\033[95m'
	BOLD   = '\033[1m'
	GREEN  = '\033[92m'
	fin    = "\033[0m"

print("""%s\t___      _____  ___ _   _
	| \{0}    // ____ |__ | \ |
	|_//o   {1}\____/ |__ |  \|%s%sv{2}%s
	%s=============================%s
{3}""".format(one, two, version, inf) % (color_con.YELLOW, color_con.fin, color_con.RED, color_con.fin, color_con.GREEN, color_con.fin))

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--numero", help = "Cuantas fechas desea generar: # default[20]", type = int) 
parser.add_argument("-f", "--formato", help = "Formatos disponibles: a = [dd:mm:yyyy], b = [yyyy:mm:dd], c = [yyyy:dd:mm] default:[a]",type = str, required = False )# or required=True
#parser.add_argument("-e", "--max", help = "La fecha Max por defecto es la actual:<[dd:mm:yyyyy] [{}]>".format(time.asctime()),type = str, required = False)
parser.add_argument("-i", "--min", help = "Fecha de inicio [dd:mm:yyyyy] por defecto es [1:1:2018] ",type = str, required = False )
parser.add_argument("-l", "--archivo", help = "Guardar fechas en archivo externo: [CSV|txt] default:[None]", type=str, required = False)
args = parser.parse_args()

def gen(d = 1, m = 1, y = 2018, numero = 20, formate = 'a'):

	print(name)

	dt_year		= datetime.now().year
	dt_month 	= datetime.now().month
	dt_day		= datetime.now().day

	i = [[str(rint(d, dt_day)), str(rint(m, dt_month)), str(rint(y, dt_year))] for _ in range(numero)]
	j = [[str(rint(y, dt_year)), str(rint(m, dt_month)), str(rint(d, dt_day))] for _ in range(numero)]
	k = [[str(rint(y, dt_year)), str(rint(d, dt_day)), str(rint(m, dt_month))] for _ in range(numero)]

	if formate == 'A' or formate == 'a':
		print("=====  =====  =====\nDias - Meses - Años\n")
		for n in i:
			print(n[0] + slash + n[1] + slash + n[2])
			if args.archivo:
				list_alterned.append(n)

	elif formate == 'B' or formate == 'b':
		print("=====  =====  =====\nAños - Meses - Dias\n")
		for n in j:
			print(n[0] + slash + n[1] + slash + n[2])
			if args.archivo:
				list_alterned.append(n)

	elif formate == 'C' or formate == 'c':
		print("=====  =====  =====\nAños - Dias - Meses\n")
		for n in k:
			print(n[0] + slash + n[1] + slash + n[2])
			if args.archivo:
				list_alterned.append(n)

	return ''

### cuando a una funcion no le pasas un argumento pero el arguento fue declarado dentro de la estructura de la funcion, el resultado en boleano es False y cuando si le pasas es True
"""def txt():
	print('f_txt')with open('gen_file.txt', 'w') as file1:
					file1.write()
"""	

def ab():
	the_file_is = 'gen_file.txt'
	gen(d = int(a1), m = int(a2), y = int(a3), numero = args.numero, formate = args.formato)	
	with open(the_file_is, 'w') as file1:
		if os.path.exists(file1.name):
			print(type(file1.name))
			existe_archivo = str(input("ingresar nombre para el archivo: {} \n %s[yes - not] %s".format(file1.name) % (color_con.PURPLE, color_con.fin)))
			if existe_archivo == 'yes':
				the_file_is = str(input('%sFile_name:%s'% (color_con.YELLOW, color_con.fin)))
				file1.write(str(list_alterned))
				print('error al renonbrar archivo:{} \n %sthe file .\{} created successful%s'.format(file1.name, file1.name) % (color_con.GREEN, color_con.fin))
			elif existe_archivo == 'not':
				file1.write(str(list_alterned))
				print('%sthe file .\{} was created successful%s'.format(file1.name) % (color_con.GREEN, color_con.fin))
			else:
				print('%sopcion invalida%s' % (color_con.RED, color_con.fin))

if args.numero:
	if args.formato == 'a':
		if args.min: #args.min:
			a1, a2, a3 = args.min.split(':')
			#b1, b2, b3 = args.max.split(':')
			if args.archivo == 'txt':
				ab()
			else:
				gen(d = int(a1), m = int(a2), y = int(a3), numero = args.numero, formate = args.formato)
		else:
			gen(numero = args.numero, formate = args.formato)
	elif args.formato == 'b':
		if args.min:
			a1, a2, a3 = args.min.split(':')
			if args.archivo == 'txt':
				ab()
			else:
				gen(d = int(a1), m = int(a2), y = int(a3), numero = args.numero, formate = args.formato)
		else:
			gen(numero = args.numero, formate = args.formato)
	elif args.formato == 'c':
		if args.min:
			a1, a2, a3 = args.min.split(':')
			if args.archivo == 'txt':
				ab()
			else:
				gen(d = int(a1), m = int(a2), y = int(a3), numero = args.numero, formate = args.formato)
		else:
			gen(numero = args.numero, formate = args.formato)
	else:	
		gen(numero = args.numero)
else:
	print(usage)

