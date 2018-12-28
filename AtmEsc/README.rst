Atmospheric Escape in the TRAPPIST-1 Planetary System
============

Overview
--------

Water photolysis, hydrogen escape, and oxygen buildup on the TRAPPIST-1 planets
as predicted by `vplanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_.

===================   ============
**Date**              12/27/18
**Author**            Rory Barnes
**Modules**           AtmEsc, STELLAR
**Approx. runtime**   20 seconds
**Source code**       `vplanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_,
                      `vplot <https://github.com/VirtualPlanetaryLaboratory/vplot>`_
===================   ============

To run this example
-------------------

.. code-block:: bash

  vplanet vpl.in
  python makeplot.py <pdf | png>

Expected output
---------------

.. figure:: Trappist1.atmesc.png
   :width: 600px
   :align: center

Atmospheric evolution of the TRAPPIST-1 planets as modified by the evolving host star. Planetary parameters are from `Grimm et al. (2018) <https://ui.adsabs.harvard.edu//#abs/2018A&A...613A..68G/>`_. *Top Left:* Bolometric stellar luminosity. *Top Right:* Stellar XUV luminosity. *Middle Left:* Stellar effective temperature. *Middle Right:* Habitable zone evolution. Dashed lines are the empirical limits and solid are the conservative limits (`Kopparapu et al. 2013 <https://ui.adsabs.harvard.edu//#abs/2013ApJ...765..131K/abstract>`_). *Bottom Left:* Surface/atmospheric water content in units of terrestrial oceans. *Bottom Right:* Oxygen buildup, assuming no sinks.  
