#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Created by Jorge L. Herrera

import random

from .data import NA, AP, SP

class genName(object):
    def __init__(self):
        pass
    def geName(self, cant, fmt, save = False):
        ini = 0
        tmp = []
        if fmt == 'a' or fmt == 'A':
            if save:
                return tmp

            else:
                for _ in range(cant):
                    tmp.append(' '.join([random.choice(NA), random.choice(AP), random.choice(SP)]))
                    print(tmp[ini])
                    ini += 1
                return ''

        if fmt == 'b' or fmt == 'B':	
            if save:
                return tmp
                
            else:
                for _ in range(cant):
                    tmp.append(' '.join([random.choice(AP), random.choice(SP), random.choice(NA)]))
                    print(tmp[ini])
                    ini += 1
                return ''
