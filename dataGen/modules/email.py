#!/usr/bin/env python3
#-*- Coding:UTF-8 -*-
# Created by: Jorge Herrera

import random

from .data import *

class genEmail(object):

    def __init__(self):
        pass

    def gEmail(self, cant, MayMin, log, save):

        log     = False if log is None else True
        tmp     = []
        gend    = [
                    '@gmail.com',
                    '@hotmail.com',
                    '@live.com',
                    '@yahoo.com'
                  ]

        if log:
            for _ in range(cant):
                tmp.append(''.join([random.choice(NA), 
                            random.choice(AP),
                            random.choice(SP),
                            str(random.randint(1, 50)), 
                            random.choice(gend)])
            )

        else:
            
            for _ in range(cant):
                tmp.append(''.join([random.choice(NA), 
                            random.choice(AP),
                            str(random.randint(1, 50)), 
                            random.choice(gend)])
            )
            
        # MAYUSC
        
        if MayMin == 'm' or MayMin == 'M':
            if save:
                return tmp
            else:
                for i in tmp:
                    # join(index of i to char @ after just show uppercase) 
                    print(''.join([i[0:i.find('@')].upper(), i[i.find("@"):len(i)]]))
                return ''
        # minuscula
        else:
            if save:
                return tmp
            else:   
                for i in tmp:
                    # join(index of i to char @ after just show lowercase)
                    print(''.join([i[0:i.find('@')].lower(), i[i.find("@"):len(i)]]))
                return ''





