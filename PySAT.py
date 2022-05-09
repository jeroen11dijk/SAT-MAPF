from pysat.solvers import Glucose3
from pysat.formula import CNF
from pysat.formula import WCNF
from pysat.card import *

vars = [1, 2, 3, 4, 5]
main = CNF()
main.append(vars)
print(main.nv)
cnf = CardEnc.equals(lits=vars, top_id=main.nv, bound=2)
cnf.to_file('another-file-name.cnf')
main.extend(cnf.clauses)
g = Glucose3()
g.append_formula(main)
g.solve()
print(g.get_model())
