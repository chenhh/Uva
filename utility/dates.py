# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    return leap