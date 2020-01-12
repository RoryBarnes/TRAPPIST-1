import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
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

#Typical plot parameters that make for pretty plot
mpl.rcParams['figure.figsize'] = (6.5,6.5)
mpl.rcParams['font.size'] = 12.0

# Load data
output = vpl.GetOutput()
time=output.star.Time

# Plot
fig, axes = plt.subplots(nrows=3, ncols=2)
#plt.figure(figsize=(4,9))
color = "k"

## Top Left: Luminosity ##
axes[0,0].plot(time, output.star.Luminosity,'k')

# Format
axes[0,0].set_xlim(1e6,time.max())
axes[0,0].set_ylim(1e-4,0.06)
axes[0,0].set_xlabel("Time [yr]")
axes[0,0].set_ylabel(r"Luminosity (L$_\odot$)")
axes[0,0].set_xscale('log')
axes[0,0].set_yscale('log')

## Top Right: XUV Luminosity ##
axes[0,1].plot(time, output.star.LXUVTot,'k')

# Format
axes[0,1].set_xlim(1e6,time.max())
axes[0,1].set_ylim(1e-8,1.1*output.star.LXUVTot.max())
axes[0,1].set_xlabel("Time [yr]")
axes[0,1].set_ylabel(r"L$_{XUV}$ (L$_\odot$)")
axes[0,1].set_xscale('log')
axes[0,1].set_yscale('log')

## Middle Left: Effective Temperature ##
axes[1,0].plot(time, output.star.Temperature,'k')

# Format
axes[1,0].set_xlim(1e6,time.max())
axes[1,0].set_ylim(0.95*output.star.Temperature.min(),1.05*output.star.Temperature.max())
axes[1,0].set_xlabel("Time [yr]")
axes[1,0].set_ylabel(r"T$_{eff}$ (K)")
axes[1,0].set_xscale('log')

## Middle Right: Habitable Zone ##
axes[1,1].plot(time, output.star.HZLimRecVenus,'g',linestyle='dashed')
axes[1,1].plot(time, output.star.HZLimRunaway,'g')
axes[1,1].plot(time, output.star.HZLimMaxGreenhouse,'g')
axes[1,1].plot(time, output.star.HZLimEarlyMars,'g',linestyle='dashed')

# Format
axes[1,1].set_xlim(1e6,time.max())
axes[1,1].set_ylim(0.005,0.1)
axes[1,1].set_xlabel("Time [yr]")
axes[1,1].set_ylabel("Hab. Zone (AU)")
axes[1,1].set_xscale('log')

# Add planets
axes[1,1].plot([0,5e9],[0.01154775,0.01154775],'k')
axes[1,1].plot([0,5e9],[0.01581512,0.01581512],color=vpl.colors.red)
axes[1,1].plot([0,5e9],[0.02228038,0.02228038],color=vpl.colors.orange)
axes[1,1].plot([0,5e9],[0.02928285,0.02928285],color=vpl.colors.pale_blue)
axes[1,1].plot([0,5e9],[0.03853361,0.03853361],color=vpl.colors.purple)
axes[1,1].plot([0,5e9],[0.04687692,0.04687692],color=vpl.colors.dark_blue)
axes[1,1].plot([0,5e9],[0.06193488,0.06193488],color='grey')
axes[1,1].set_yticks([0.01,0.05,0.1])

## Bottom Left: Surface water ##
axes[2,0].plot(time, output.b.SurfWaterMass,'k')
axes[2,0].plot(time, output.c.SurfWaterMass,color=vpl.colors.red)
axes[2,0].plot(time, output.d.SurfWaterMass,color=vpl.colors.orange)
axes[2,0].plot(time, output.e.SurfWaterMass,color=vpl.colors.pale_blue)
axes[2,0].plot(time, output.f.SurfWaterMass,color=vpl.colors.purple)

# Format
axes[2,0].set_xlim(1e6,time.max())
axes[2,0].set_ylim(0,11)
axes[2,0].set_xlabel("Time [yr]")
axes[2,0].set_ylabel("Surface Water (TO)")
axes[2,0].set_xscale('log')

## Bottom Right: Abiotic Oxygen ##
axes[2,1].plot(time, output.b.OxygenMass,'k',label='b')
axes[2,1].plot(time, output.c.OxygenMass,color=vpl.colors.red,label='c')
axes[2,1].plot(time, output.d.OxygenMass,color=vpl.colors.orange,label='d')
axes[2,1].plot(time, output.e.OxygenMass,color=vpl.colors.pale_blue,label='e')
axes[2,1].plot(time, output.f.OxygenMass,color=vpl.colors.purple,label='f')
axes[2,1].legend(loc='best',prop={'size': 11})

# Format
axes[2,1].set_xlim(1e6,time.max())
axes[2,1].set_ylim(0,2000)
axes[2,1].set_xlabel("Time [yr]")
axes[2,1].set_ylabel("Atm. Oxygen (bar)")
axes[2,1].set_xscale('log')

# Final formating
fig.tight_layout()

if (sys.argv[1] == 'pdf'):
    fig.savefig('Trappist1.atmesc.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('Trappist1.atmesc.png', bbox_inches="tight", dpi=600)
