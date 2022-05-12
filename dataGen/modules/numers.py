#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# Created by Jorge l.


from random import randint as rint
from datetime import datetime


class genNum:
	""" Genera numeros de todo tipo """

	def __init__(self, typeGen):
		self.typeGen = typeGen

	def dninum(self, cantidad, save = False):
		dt = [str(rint(0, 9)) + str(rint(100, 989)) + str(rint(100, 989)) + str(rint(0, 9)) for _ in range(cantidad)]
		
		if save:
			return dt
		
		else:
			for i in dt:
				print(i)
			return ''

	def celnum(self, cantidad, prefix = '+51', save = False):
		# prefix = '51' default
		print('Generating numbers...')
		x = [[str(9) + str(rint(20, 99)), str(rint(110, 989)), str(rint(110, 989))] for i in range(cantidad)]
		
		if save:
			return x
		
		else:
			for i in x:
				print(prefix + ' ' + ' '.join(i))


		




















