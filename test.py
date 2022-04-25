from ortools.sat.python import cp_model

model = cp_model.CpModel()
a, b, c, d = [model.NewBoolVar(x) for x in 'abcd']
q = [a, b]
model.Add(sum(q) == 2)

solver = cp_model.CpSolver()
solver.Solve(model)

for x in [a, b, c, d]:
    print(solver.Value(x))