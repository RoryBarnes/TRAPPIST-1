#!/usr/bin/python
import numpy as np
import subprocess as subp
import string
#import matplotlib.pyplot as plt

def GetLogValue(file,body,param):
    logfile=open(file)
    current=0
    for line in logfile:
        words=str.split(line)
        if len(words) > 1:
            if 'BODY' in words[1]:
                if body == words[2]:
                    current=1
            if current == 1 and param in words[0]:
                last=len(words)-1
                return words[last]


emin=1e-5
emax=0.2
de=1.01
npl=7

e=emin
necc=0
while e <= emax:
    necc += 1
    e *= de

#print(necc)

heat=[[0 for j in range(necc)] for k in range(npl)]
ecc=[0 for j in range(necc)]

name = ['b','c','d','e','f','g','h']
infile =['b.tmp','c.tmp','d.tmp','e.tmp','f.tmp','g.tmp','h.tmp']
outfile =['b.in','c.in','d.in','e.in','f.in','g.in','h.in']
heatfile=open('trappist1.tideheat.out','w')

e=emin
n=0
while e <= emax:
    ecc[n] = e
    for j in range(npl):
        cmd1="cp "+infile[j]+" "+outfile[j]
        subp.call(cmd1,shell=True)
        cmd2="echo dEcc    "+repr(e)+" >> "+outfile[j]
        subp.call(cmd2,shell=True)
    #exit()
    cmd3="vplanet vpl.in >& dump"
    subp.call(cmd3,shell=True)

    # Now get heat fluxes
    #print(n)
    heatfile.write(repr(e)+' ')
    for j in range(npl):
        heat[j][n] = float(GetLogValue('trappist1.log',name[j],'SurfEnFluxEqtide'))
        heatfile.write(repr(heat[j][n])+' ')
        #print(heat[j][0])
    heatfile.write('\n')
    n += 1
    e *= de
    #exit()



#plt.plot(ecc,heat[0])
#plt.savefig('trappist1.tidalheat.png')
