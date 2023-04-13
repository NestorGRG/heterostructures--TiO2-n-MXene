from copy import deepcopy
from ase.io import read,write
from ase.build import add_adsorbate,rotate,sort
from ase.visualize import view

#Reading the structure files
mxene = read("MXenes/CONTCAR-Ti2C")
np = read("TiO2-NP/POSCAR-tio2-n5")

#How many replicas of MXene?
nx,ny=input("Size of the unitcell? (NxN) ").split("x")
nx=int(nx)
ny=int(ny)
mxene *= (nx,ny,1)

#Defining the Center of Mass
commxe= mxene.get_center_of_mass(scaled=False)
commnp= np.get_center_of_mass(scaled=False)

for i in range(0,150,10):

    #Creating a copy of the building blocks
    nano=deepcopy(np)
    slab=deepcopy(mxene)

    #Rotating the NP
    nano.rotate("z",i, center="COM", rotate_cell=False)
    nano.center(axis=(0,1,2))

    #Creating the heterostructure
    add_adsorbate(slab=slab, adsorbate=nano, height=2.5, position=(commxe[0],commxe[1]),mol_index=6)

    #Writing POSCAR files of the heterostructures
    slab_sorted=sort(slab)
    name="POSCAR-z-"+str(i)
    write(name, slab_sorted, format="vasp")

    #View the results
    #view(slab)

    #Clearing the variable slab and nano in order to not superpose the adsorbants and rotations
    del slab
    del nano