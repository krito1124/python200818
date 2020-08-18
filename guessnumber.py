# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:01:25 2020

@author: USER
"""

import random
num=random.randint(1,20)
i=0
while i<5:
    ans=int(input("please enter number:"))
    if ans == num:
        print ("that's right")
        print (i,"times")
        break
    elif num >ans:
        print("bigger")
        i=i+1
    elif num <ans:
        print("smaller")
        i=i+1
    else:
        print("wrong")
        print("+1")
        i=i+1

