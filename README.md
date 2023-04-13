# Heterostructures (TiO<sub>2</sub>)<sub>n</sub>@MXene
Programs to generate heterostructure POSCARs from two building blocks: TiO<sub>2</sub> nanoparticles and MXene slabs

### NOTE: all input files must be in the same directory where the program is

## Needed Files
The necessary input files are:
  1.  `MXene_POSCAR`
  2.  `TiO2_POSCAR`
With the variable `mxene` and `np`, put the names or paths of your input files

## Requirements  
The following Python modules must be installed:
  1. `ASE`

## hetero-z-n5.py
This program generates a set of POSCAR files of heterostructures, where each heterostructure has been created adsorbing the nanoparticle on the MXene slab and rotate from 0 to 140 degrees by tens through the `z` axis. The position of the adsorption process is in the center of mass of the MXene slab

### Instructions
1.  Make sure that you put the names or paths of your input files in the `mxene` and `np` variables.
2.  The above mentioned python modules are installed.
3.  Run the program with Python.
4.  The user is asked for the dimension of the cell with the displayed format, e.g. 5x5, 6x6, 7x7.
5.  The user is free to modify the angles of rotation within the `for` loop in Rotating section of the program.
6.  The user is free to modify the atom which the nanoparticle is adsorbed thought with the `add_adsorbate()` function, with the `mol_index` tag.

## hetero-face-n35.py

### Instructions
1.  Make sure that you put the names or paths of your input files in the `mxene` and `np` variables.
2.  The above mentioned python modules are installed.
3.  Run the program with Python
4.  The user is asked for the dimension of the cell with the formad displayed, e.g. 5x5, 6x6, 7x7
5.  The user is free to add the desired vacuum width value with the `vacuum_value` variable.
6.  Due to the symmetry of the Nanoparticle used as example (tetragonal dipyramid), the particle is rotated in order to adsorb it throught one of its faces with the `nano.rotate()` function
7.  The user is free to modify the atom which the nanoparticle is adsorbed thought with the `add_adsorbate()` function, with the `mol_index` tag.
