from copy import deepcopy
from ase.io import read,write
from ase.build import add_adsorbate,add_vacuum,rotate,sort
from ase.visualize import view
from ase.constraints import FixAtoms

#Reading the structure files
mxene = read("MXenes/CONTCAR-Ti2C")
np = read("TiO2-NP/tio2-n35.xyz")

#How many replicas of MXene?
nx,ny=input("Size of the unitcell? (NxN) ").split("x")
nx=int(nx)
ny=int(ny)
mxene *= (nx,ny,1)

#Defining the Center of Mass
commxe= mxene.get_center_of_mass(scaled=False)
commnp= np.get_center_of_mass(scaled=False)

#Creating a copy of the building blocks
nano=deepcopy(np)
slab=deepcopy(mxene)

#Rotating the NP
nano.rotate("y",65, center="COM", rotate_cell=False)
nano.center(axis=(0,1,2))

#Creating the heterostructure
add_adsorbate(slab=slab, adsorbate=nano, height=8.5, position=(commxe[0]+5,commxe[1]),mol_index=77)
vacuum_value = 15
add_vacuum(slab, vacuum_value)

#Adding a constrain for selective dynamics and sorting it
slab_sorted=sort(slab)
# z_coords = slab_sorted.positions[:, 2]
# mask = z_coords < 8.0
# constraint = FixAtoms(mask=mask)
# slab_sorted.set_constraint(constraint)

#Writing POSCAR files of the heterostructures
name= "heterostructure-face-n35-"+str(nx)+"x"+str(ny)
write(name, slab_sorted, format="vasp", vasp5=True, direct=False)

#View the results
#view(slab)

#Clearing the variable slab and nano in order to not superpose the adsorbants and rotations
del slab
del nano

