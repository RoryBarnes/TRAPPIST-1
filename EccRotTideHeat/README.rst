Tidal Heating of the TRAPPIST-1 e due to rotation and eccentricity
============

Overview
--------

Tidal heating of the TRAPPIST-1 e as predicted by the eqtide module in
`VPLanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_.

===================   ============
**Date**              08/28/2020
**Author**            Rory Barnes
**Modules**           EqTide
**Approx. runtime**   100 seconds
**Source code**       `vplanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_,
                      `vplot <https://github.com/VirtualPlanetaryLaboratory/vplot>`_
===================   ============

To run this example
-------------------

.. code-block:: bash

  vspace vspace.in
  multi-planet vspace.in
  python makeplot.py <pdf | png>

Expected output
---------------

.. figure:: EccRotHeat.png
   :width: 600px
   :align: center

Surface energy flux in W/m^2 due to tides as a function of eccentricity and
rotation period. The tidal Q is 100 and the Love number of degree 2 is 0.3. 
