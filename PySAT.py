from pysat.card import *
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
from pysat.solvers import Glucose3
wcnf = WCNF()

wcnf.append([1], weight=-1)
wcnf.append([2], weight=-1)
wcnf.append([3], weight=-1)
wcnf.append([4])
wcnf.append([-4, -1])
wcnf.append([-5, 2])
rc2 = RC2(wcnf)
wcnf.to_file('another-file-name.cnf')
model = rc2.compute()
print(model)
print(rc2.cost)
rc2.delete()
