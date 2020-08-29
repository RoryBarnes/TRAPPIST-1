Tidal Heating of the TRAPPIST-1 Planets
============

Overview
--------

Tidal heating of the TRAPPIST-1 planets as predicted by the constant-phase-lag
model in `VPLanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_.

===================   ============
**Date**              01/16/2020
**Author**            Rory Barnes
**Modules**           EqTide
**Approx. runtime**   100 seconds
**Source code**       `vplanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_,
                      `vplot <https://github.com/VirtualPlanetaryLaboratory/vplot>`_
===================   ============

To run this example
-------------------

.. code-block:: bash

  python survey.py
  python makeplot.py <pdf | png>

Expected output
---------------

.. figure:: trappist1.tideheat.png
   :width: 600px
   :align: center

Surface energy flux due to tides as a function of eccentricity. The tidal Q is
100 and the Love number of degree 2 is 0.3. The values for masses, radii, and
orbital periods are from van Grootel et al. (2018) and Grimm et al. (2018). The
green region is where energy fluxes are below Earth's modern (non-tidal) flux of
80 mW/m^2 ("Earth-like"), yellow-green is for fluxes between Earth and modern Io's
of 2 W/m^2 ("Tidal Earth"), orange is fluxes between Io's and a runaway
greenhouse at 300 W/m^2 ("Super-Io"), and red is for planets in a runaway
greenhouse driven by tides ("Tidal Venus").
