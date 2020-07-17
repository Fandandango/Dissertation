from ase.io import read
from pymatgen.io.cif import CifParser, str2float
from pymatgen.vis.structure_vtk import StructureVis
from pymatgen.core.structure import Structure
from pymatgen.core.operations import SymmOp
from pymatgen.util.coord import in_coord_list_pbc
import numpy as np
import math
import os

DIR = "cifs/Large_T2_set/"
crystal = os.path.join(DIR, "job_03154.cif")
o_ = CifParser(crystal)
atoms = read(crystal)
cell = atoms.get_cell()
print(o_.as_dict())
data = o_.as_dict()['job_03154']


s = data['_atom_site_type_symbol']
xs = [str2float(x) for x in data['_atom_site_fract_x']]
ys = [str2float(x) for x in data['_atom_site_fract_y']]
zs = [str2float(x) for x in data['_atom_site_fract_z']]
c = np.array([xs, ys, zs]).T
coords = []
symbols = []
# print(data)
try:
	symops = [SymmOp.from_xyz_string(s) for s in data['_space_group_symop_operation_xyz']]
	for coord, sym in zip(c, s):
		for op in symops:
			print(op)
			new_coord = op.operate(coord)
			print(coord)
			print(new_coord)
			if not in_coord_list_pbc(coords, new_coord):
				coords.append(new_coord)
				symbols.append(sym)
except:
	for coord, sym in zip(c, s):
		coords.append(coord)
		symbols.append(sym)


s_ = Structure(cell, symbols, coords)

s1 = o_.get_structures()[0]
# print(o_.get_structures()[0].__dict__)
s = StructureVis()
s.show_polyhedron = False
s.set_structure(s_, to_unit_cell=False)
s.show()
