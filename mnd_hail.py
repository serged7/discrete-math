import numpy as np
import sympy as s
import umap
import math

from datetime import datetime as dt
from matplotlib import pyplot as plt
import csv

def conv(x):
    #print(x)
    conv = False
    l = 0
    while not conv:
        l += 1
        y = (3*x + 1)//2
        while y % 2 == 0:
            y = y//2
        if y == 1:
            conv = True
        x = y
        #print(x, l)
    return l


def comp(x):
    k = c = y = 0
    if not x % 3:
        return (-1, 0, 0)

    y = 1 if not (x - 1) % 3 else -1
    x -= y
    while not x % 2:
            k += 1
            x = x//2
    c = x
    #print('result', k, c, y)
    return (k, c, y)

def val(x):
    return 2**x[0] * x[1] + x[2]

def v2(y):
    j = 0
    while not y % 2:
        j += 1
        y = y//2
    return j
    
def trans(x):
    j = x[0]
    c = x[1]
    y = x[2]
    xt = 3**(j-1)* c + y

    return 0

def tranX(y):
    x = comp(y)
    j = x[0]
    c = x[1]
    y = x[2]
    xt = (0, 0, 0)
    xr = (0, 0, 0)
    if y > 0: # d-type
        if not j % 2: # irr d
            l = j // 2 - 1
            xt = (2, 3**l * c, y)
            jn = v2(xt[1] + y)
            cn = (xt[1] + y)/2**v2(xt[1] + y)
            cn = 3*int(cn)
            xr = (jn, cn, -y)
            print("irr d", x, xt, xr)  # dd verified
        else:
            l = (j - 1) // 2
            xt = (1, 3**l * c, y)
            jn = v2(xt[1] + y)
            cn = (xt[1] + y)/2**v2(xt[1] + y)
            cn = 3*int(cn)
            xr = (jn, cn, -y)
            print("st d", x, xt, xr)   # ds verified
    else: # a-type  
        xt = (1, 3**(j-1) * c, y)
        #print("v2", v2(xt[1] - 1), 3*int((xt[1] + y)/2**v2(xt[1] + y)))
        if v2(xt[1] - 1) == 1: # irr a
            jn = v2(xt[1] + y)
            cn = (xt[1] + y)/2**v2(xt[1] + y)
            cn = 3*int(cn)
            xr = (jn, cn, -y)
            print("irr a", x, xt, xr)  # ad verified
        else:
            jn = v2(xt[1] + y) - 1
            cn = (xt[1] + y)/2**v2(xt[1] + y)
            cn = 3*int(cn)
            xr = (jn, cn, -y) 
            print("st a", x, xt, xr)   # as verified
    #print("ta", x, val(x), xt, val(xt), xr, val(xr))

    return xr

            
def main():
    tc = 0
    x = 99 #119 (ad) 121 673 (ds) 337 (dd) 137 (as)
    x = int(input("number?"))
    xm = x
    if not x % 3:
        x = (3*x + 1)//2
        while not x % 2:
            x //= 2
    if x == 1:
        print("converged: ", xm, x)
    else:
        print("begin", x, comp(x))

    while tc < 50:
        tc += 1
        y = tranX(x)
        print("transition:", tc, x, comp(x), val(y), y)
        x = val(y)
        if x == 1:
            print("converged", tc, x)
            break
        
    print("result:", tc, xm, x)
    print(dt.now())

main()
            
        
