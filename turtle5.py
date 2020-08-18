# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:10:41 2020

@author: USER
"""
import turtle



z = int(input("請輸入邊形"))
for i in range(z):
    turtle.forward(50)
    turtle.right(360/z)
turtle.done()