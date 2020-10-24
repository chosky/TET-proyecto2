#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
22/10/2020
--------------------------------------
@author: Cristian Aristizabal Giraldo
--------------------------------------
Version libs
--------------------------------------
numpy = 1.18.3
"""


#import lib
import numpy as np
import time
import sys

#args
size = int(sys.argv[1])
iter = int(sys.argv[2])

# alive = 1; dead = 0
# Intialize board random
status = np.random.randint(2, size=(size, size))

#size board
nX, nY = size, size

running = True
i = 0
while running and i < iter:

    newStatus = np.copy(status) # Copy status


    for x in range(0,nX):
        for y in range(0,nY):

            # Num neighbors
            nNeigh = status[(x-1)%nX,(y-1)%nY] + status[(x)%nX,(y-1)%nY] + \
                    status[(x+1)%nX,(y-1)%nY] + status[(x-1)%nX,(y)%nY] + \
                    status[(x+1)%nX,(y)%nY] + status[(x-1)%nX,(y+1)%nY] + \
                     status[(x)%nX,(y+1)%nY] + status[(x+1)%nX,(y+1)%nY]

            # Rule 1: cell alive
            if status[x,y] == 0 and nNeigh==3:
                newStatus[x,y] = 1

            # Rule 2: cell dead
            elif status[x,y] == 1 and (nNeigh < 2 or nNeigh > 3):
                newStatus[x,y] = 0


    status = np.copy(newStatus)

    stringPrint = ''
    for x in range(0, nX):
        for y in range(0, nY):

            if newStatus[x, y] == 1:
                stringPrint = stringPrint + '*'
            else:
                stringPrint = stringPrint + '.'

        stringPrint = stringPrint + '\n'

    print(stringPrint)
    print(nX*'=')

    i = i + 1

