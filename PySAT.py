from pysat.card import *
from pysat.solvers import Glucose3

vars = [1, 2, 3, 4, 5, 6, 7, 8]

main = CNF()
main.append(vars)
print(main.nv)
cnf = CardEnc.equals(lits=vars, top_id=main.nv, bound=1)
print(cnf.nv)
cnf.to_file('another-file-name.cnf')
main.extend(cnf.clauses)
g = Glucose3()
g.append_formula(main)
g.solve()
print(g.get_model())
