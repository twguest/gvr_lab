#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:34:06 2021

now this is in english
@author: twguest
"""


from functions import hello_world

def routine(n):
    
    for i in range(n):
        hello_world()
        
        
if __name__ == '__main__':
    routine(10)
