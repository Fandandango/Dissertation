import ase.io
import os
from scipy.spatial import Voronoi
import numpy as np


# set path to the directory containing cif file
# leave as '' if file is in same directory as this file
# path = 'cifs/Large_T2_set'
path = "cifs/T2_experimental/"
# filename = 'job_00001.cif'
filename = "DEBXIT02_1478361_T2gamma_450K.cif"
atoms = ase.io.read(os.path.join(path, filename))
print(atoms)

# atoms = ase.io.read("job_03351.cif")

from draw import draw
draw(atoms, unwrap=False)
