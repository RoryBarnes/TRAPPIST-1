#!/usr/bin/python
import numpy as np
import subprocess as subp
import string as str
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys
try:
    import vplot as vpl
except:
    print('Cannot import vplot. Please install vplot.')

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

file=open('trappist1.tideheat.out')
nlines=996

e=[0 for j in range(nlines)]
hb=[0 for j in range(nlines)]
hc=[0 for j in range(nlines)]
hd=[0 for j in range(nlines)]
he=[0 for j in range(nlines)]
hf=[0 for j in range(nlines)]
hg=[0 for j in range(nlines)]
hh=[0 for j in range(nlines)]

j=0
for line in file:
    words=line.split()
    e[j]=float(words[0])
    hb[j]=float(words[1])
    hc[j]=float(words[2])
    hd[j]=float(words[3])
    he[j]=float(words[4])
    hf[j]=float(words[5])
    hg[j]=float(words[6])
    hh[j]=float(words[7])
    j += 1

fig = plt.figure(figsize=(10,8), dpi=300)
ax=fig.add_subplot(1,1,1)
fig.subplots_adjust(wspace=.05,left=.01,bottom=.01)

#ax.spines['top'].set_color('white')
#ax.spines['top'].set_linewidth(2)
#ax.spines['right'].set_color('white')
#ax.spines['right'].set_linewidth(2)
#ax.spines['bottom'].set_linewidth(2)
#ax.spines['bottom'].set_color('white')
#ax.spines['left'].set_color('white')
#ax.spines['left'].set_linewidth(2)

#ax.title.set_color('white')
#ax.yaxis.label.set_color('white')
#ax.xaxis.label.set_color('white')
#ax.tick_params(axis='x', which ='both',colors='white')
#ax.tick_params(axis='y', which = 'both',colors='white')

plt.rcParams['axes.linewidth'] = 3
plt.xlim(0.001,0.1)
plt.ylim(1e-3,1000)
#plt.xscale('log')
plt.yscale('log')
plt.tick_params(axis='both', labelsize=20,width=3,length=10,top='on',right='on')
plt.xlabel('Eccentricity',fontsize=25)
plt.ylabel('Surface Energy Flux (W/m$^2$)',fontsize=25)

#plt.fill_betweenx([1e-5,0.2],[1e-5,0.2],[1e-5,0.08],color='0.85', **fbk)
ax.add_patch(patches.Rectangle((1e-5,1e-5),0.2,0.08,color='#2C6F4C'))
ax.add_patch(patches.Rectangle((1e-5,0.08),0.2,2.92,color='#cc9900'))
ax.add_patch(patches.Rectangle((1e-5,3),0.2,297,color='#ff9933'))
ax.add_patch(patches.Rectangle((1e-5,300),0.2,700,color='#cc0000'))


plt.plot(e,hb,color='w',linewidth=3)
plt.text(0.012,350,'b',color='w',fontsize=25)

plt.plot(e,hc,color='w',linewidth=3)
plt.text(0.013,70,'c',color='w',fontsize=25)

plt.plot(e,hd,color='w',linewidth=3)
plt.text(0.015,3,'d',color='w',fontsize=25)

plt.plot(e,he,color='w',linewidth=3)
plt.text(0.016,0.7,'e',color='w',fontsize=25)

plt.plot(e,hf,color='w',linewidth=3)
plt.text(0.018,0.15,'f',color='w',fontsize=25)

plt.plot(e,hg,color='w',linewidth=3)
plt.text(0.021,0.05,'g',color='w',fontsize=25)

plt.plot(e,hh,color='w',linewidth=3)
plt.text(0.035,0.004,'h',color='w',fontsize=25)

fig.tight_layout()

if (sys.argv[1] == 'pdf'):
    fig.savefig('Trappist1.tidheat.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('Trappist1.tideheat.png', bbox_inches="tight", dpi=600)

plt.close()
