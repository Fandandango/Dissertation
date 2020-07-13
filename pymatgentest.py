from ase.io import read
from pymatgen.io.cif import CifParser, str2float
from pymatgen.vis.structure_vtk import StructureVis
from pymatgen.core.structure import Structure
from pymatgen.core.operations import SymmOp
from pymatgen.util.coord import in_coord_list_pbc
import numpy as np
import math

o_ = CifParser('T2experimental/T2epsilon.cif')
atoms = read('T2experimental/T2epsilon.cif')
cell = atoms.get_cell()
data = o_.as_dict()['ttbi_sub']


s = data['_atom_site_type_symbol']
xs = [str2float(x) for x in data['_atom_site_fract_x']]
ys = [str2float(x) for x in data['_atom_site_fract_y']]
zs = [str2float(x) for x in data['_atom_site_fract_z']]
c = np.array([xs, ys, zs]).T
coords = []
symbols = []
# print(data)
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


s_ = Structure(cell, symbols, coords)


s1 = o_.get_structures()[0]
# print(o_.get_structures()[0].__dict__)
s = StructureVis()
s.show_polyhedron = False
s.set_structure(s_, to_unit_cell=False)
s.show()
