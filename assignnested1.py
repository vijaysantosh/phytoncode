# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 07:28:45 2021

@author: VIJAY SANTHOSH
"""

for r in range(7):
    if r % 2 == 0:
        for c in range(1, 7):
            if c % 2 == 1:
                if c != 5:
                    print(" ", end=" ")
                else:
                    print(" ")

            else:
                print("|", end=" ")
    else:
        print("--------")