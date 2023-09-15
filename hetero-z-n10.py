from copy import deepcopy
import os
from ase.io import read,write
from ase.build import add_adsorbate,rotate,sort
from ase.visualize import view

# Reading the structure files

np = read("TiO2-NP/tio2-n10.xyz")

# How many replicas of MXene?
nx,ny=input("Size of the unitcell? (NxN) ").split("x")
nx=int(nx)
ny=int(ny)

mxene = read("MXenes/CONTCAR-Ti2C")
mxene *= (nx,ny,1)

# Defining the Center of Mass
commxe= mxene.get_center_of_mass(scaled=False)
commnp= np.get_center_of_mass(scaled=False)

#Rotating the NP
#through the largest face
np.rotate("y",65, center="COM", rotate_cell=False)
np.center(axis=(0,1,2))

# Rotating
for i in range(0,150,10):

    # Creating a copy of the building blocks
    nano=deepcopy(np)
    slab=deepcopy(mxene)

    # Rotating the NP
    nano.rotate("z",i, center="COM", rotate_cell=False)
    nano.center(axis=(0,1,2))

    # Creating the heterostructure
    add_adsorbate(slab=slab, adsorbate=nano, height=5, position=(commxe[0],commxe[1]),mol_index=6)

    # Writing POSCAR files of the heterostructures
    slab_sorted=sort(slab)
    name="heterostructures-n10/POSCAR-z-"+str(i)
    write(name, slab_sorted, format="vasp")

    # View the results
    # view(slab)

    # Clearing the variable slab and nano in order to not superpose the adsorbants and rotations
    del slab
    del nano
del mxene