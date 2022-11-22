|build| |coverage| |docs| |pypi| |zenodo| 

.. inclusion-marker-do-not-remove


This code is my little contribution to the code that you can find in https://github.com/galform/get_nebular_emission. It is not finished here.

TO DO
-----
[] Calculate Bulge and Disk separately and then add the fluxes from the 2 contributions.
[] Adding AGN lines. From Cedric: For Galform, we should try to do this in a way that the spectrum and luminosity of the ionizing radiation assumed in the emission lines calculation is consistent with the AGN SED assumed in Galform. Currently we use an AGN template spectrum from Marconi, for which the shape depends on the AGN bolometric luminosity. Andrew updated the Galform code so that it calculated observer-frame magnitudes for any bands of interest, along with observer-frame luminosities in hard and soft X-ray bands, for outputs at snapshots, based on the Marconi template (which depends on bolometric luminosity). We should check that this is properly included in the main version of Galform on the archive, and that it works correctly. Andrew was still working on calculating AGN luminosities correctly on lightcones (the issue being that AGN luminosities do not vary smoothly between snapshots) when he left, so I don't think there is code for that yet.


   
Get nebular emission
======================

**get_nebular_emission** is a Python package that given the metallicity of cold gas, the stellar mass and either the specific star formation or the number of ionizing photons, calculates the intensity of nebular emission lines from star forming HII regions.


The code will read galaxy properties from an input text file with values separated by spaces. This can have a header, as long as the header lines start with characters or signs well specify (different from the minus sign). The file can contain several columns with properties for different galactic components. For each component, the column number (starting from 0) should be provided for the following properties: the stellar mass (Msun), the (instantaneous) star formation rate (SFR Msun/Gyr), the metallicity of the cold gas (defined as the ratio MZcold/Mcold).

If a h0 value is specified, then the units will be assumed to be: stellar mass (Msun/h), SFR (Msun/h/Gyr).


Example
-------

The **example.py** and **example2.py** runs over the given example data, producing a new file and a plot that compares the original and the prepared data. To run this
example, simply type: :code:`python example.py`.

Tests
-----

The test can be run using unittest:
:code:`python3 -m unittest discover -s tests`.

Requirements and Installation
-----------------------------

This code has been developed in Python 3.7.1 and it is compatible with Python above 3.5 versions. The code has been tested to run in Linux and Windows operating systems. 

This code uses numpy as specified in docs/requirements.txt. The ploting routine from the *example.py* also requires the use of matplotlib. h5py is necessary to run over hdf5 files, from eml_photio it is mandatory.

The code can be run directly from a cloned GitHub `repository`_ and then makeing a local installation from the main directory (where you can see `setup.py`:
:code:`python3 setup.py install`.


The functions in the package can be used after importing novonix_add, for example as follows:



.. _pyversion: https://uk.mathworks.com/help/matlab/getting-started-with-python.html

.. _package: https://pypi.org/project/get_nebular_emission/

.. _repository: https://github.com/galform/get_nebular_emission

.. |build| image:: https://travis-ci.org/galform/get_nebular_emission.svg?branch=master
    :target: https://travis-ci.org/galform/get_nebular_emission

.. |coverage| image:: https://codecov.io/gh/galform/get_nebular_emission/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/galform/get_nebular_emission
	     
.. |docs| image:: https://readthedocs.org/projects/get_nebular_emission/badge/?version=latest
   :target: https://get_nebular_emission.readthedocs.io/en/latest/
   :alt: Documentation Status

.. |pypi| image:: https://img.shields.io/pypi/v/get_nebular_emission.svg
    :target: https://pypi.org/project/get_nebular_emissioin/
	 
.. |zenodo| image:: https://zenodo.org/badge/186994865.svg
   :target: https://zenodo.org/badge/latestdoi/186994865

ISSUES
------
**eml_io**

· Set the program to deal with hdf5 files.

· Allow for (12 + log(O/H)) direct input.

· Search a more efficient way to do the temporary file and allow to take more or less components.

· Search a more efficient way to do the reduced_file, maybe matrix form. It is necessary the column stack for the header, maybe another function more efficient. If there is a last row in the file to reduce, that is not a list of floats but a sentence, the code gives an error, we must think a way to do not take the last row if it is not make of floats.  

· Explore star models for differents IMF for the conversion from the Lyman Continuum photons to the instantaneous SFR. Investigate the single stellar populations (SSP).

· The Baught et al. (2021) constants for the transformation from the Lyman Continuum photons to the instantaneous sSFR depend of the IMF and the SSP. We must think how it depends and move them to the eml_const module, to, in the future, allow the model to choose the constants taking into account the IMF and the SSP. 
    
**eml_une**

· Search a more efficient way to do the temporary file. Allow more or less components in the header. change the names of the header.

· Allow more models to be chosen.


**eml_photio**

· Add more things to the dicctionary to simplify the code. For example the temporary files from eml_une, we can distinguish them depending on the model. Useful in clean_photarray.

· In get_limits allow the change of units depending of the model in needed.

· Clean photarray is not too useful yet, the interpolations can be more efficient.

· Improve the way to get the limits and to put other limits depending on the model.

· In get_lines_Gutkin maybe introduce more variables in the description to give more liberty with the variables.

· In get_lines_Gutkin allow to check if there is an ongoing bulge with the masses to do the bulge interpolations or not.

· Allow the code to choose a photo-ionisation model and to deal with the interpolations.

· If the limits file does not exist, allow the program to continue the interpolations.

· Program set to do linear interpolations. See what happends with other types of interpolations.

**eml_dust**

· Create a dust module with the line attenuations.

**eml_plots**

· In test_sfrf set the program to allow several observation data and automate for every redshift, allow the change of units depending of the observational file choosen.

· In test_sfrf there is a problem with the contours, the plot is not well in my opinion. Set the program to allow automate the levels of the contours. One way to do it: In SFRF search the bin with at least 100 galaxies (before divide the data by the volume) to be the minimum level, get the maximum value of phi to be the maximum level and take another one between these two. 

· In test_medians the plots do not work, the legend is not show as wanted.

· Add test_zm. Similar to test_sfrf but with the metallicity.

· Add the command to delete the temporary files after having done the plots.

· In test_sfrf verify the limits for the SFR and the mass. 

· Put some warnings if we have data out of the limits to do the plots. 

· Put more warnings to notify the errors better.

· In the future, for verification, we could compare the mstardot_average versus the mstardot given by GALFORM and the mstardot_average versus the (mstardot + mstardot_burst). We have assumed that mstardot is the SFR averaged of the disc, so this is a way to verify this assumption.

· To do the plots there is only one sub-volume from 200. Do a loop to read all the sub-volumes to do the plots and get more realistic data. Add a flag with the glob.glob() function. This flag could ask for a snapshot and a redshift to plot all the sub-volumes with those characteristics. We must think about that because that means that the redshift and the snapshot number must be in the file name of each sub-volume and that could be restrictive.

**eml_const**

· Add the constants for the IMF and the SSP, D and B of the equations 2 and 3 of the overleaf.

**Others**

· example2.py is an example of how to run the function get_reducedfile from eml_io and the test_plots.

· Allow the escape fraction vary: (100-escf)*LyC

