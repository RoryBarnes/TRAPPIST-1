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
mpl.rcParams['figure.figsize'] = (9,4)
mpl.rcParams['font.size'] = 12.0

# Load data
output = vpl.GetOutput()
time=output.star.Time

# Plot
fig, axes = plt.subplots(nrows=1, ncols=3)
#plt.figure(figsize=(4,9))
color = "k"

ad = (output.d.SemiMajorAxis/output.d.SemiMajorAxis[0] - 1)/1e-3
ae = (output.e.SemiMajorAxis/output.e.SemiMajorAxis[0] - 1)/1e-3
af = (output.f.SemiMajorAxis/output.f.SemiMajorAxis[0] - 1)/1e-3

sd = (output.d.Instellation/output.d.Instellation[0] - 1)*1e3
se = (output.e.Instellation/output.e.Instellation[0] - 1)*1e3
sf = (output.f.Instellation/output.f.Instellation[0] - 1)*1e3

## Left: semi-major axis ##
axes[0].plot(time, ad)
axes[0].plot(time, ae,color=vpl.colors.orange)
axes[0].plot(time, af,color=vpl.colors.red)

# Format
axes[0].set_xlim(time.min(),time.max())
axes[0].set_ylim(-0.25,0.25)
axes[0].set_xlabel("Time [yr]")
axes[0].set_ylabel(r"$\Delta$ Semi-major Axis ($\times 10^3$)")

## Middle: eccentricities ##
axes[1].plot(time, output.d.Eccentricity,label='d')
axes[1].plot(time, output.e.Eccentricity,color=vpl.colors.orange,label='e')
axes[1].plot(time, output.f.Eccentricity,color=vpl.colors.red,label='f')


# Format
axes[1].set_xlim(time.min(),time.max())
axes[1].set_ylim(0.0,0.015)
axes[1].legend(loc="best")
axes[1].set_xlabel("Time [yr]")
axes[1].set_ylabel("Eccentricity")

## Right: instellation ##
axes[2].plot(time, sd)
axes[2].plot(time, se,color=vpl.colors.orange)
axes[2].plot(time, sf,color=vpl.colors.red)

# Format
axes[2].set_xlim(time.min(),time.max())
axes[2].set_ylim(-0.5,0.5)
axes[2].set_xlabel("Time [yr]")
axes[2].set_ylabel(r"$\Delta$ Instellation ($\times 10^3$)")

# Final formating
fig.tight_layout()

if (sys.argv[1] == 'pdf'):
    fig.savefig('Trappist1.NBody.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('Trappist1.NBody.png', bbox_inches="tight", dpi=600)
