import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.x = pyo.Var([1,2], domain=pyo.NonNegativeIntegers)

model.OBJ = pyo.Objective(expr = 2*model.x[1] + 3*model.x[2], sense=pyo.maximize)

model.Constraint1 = pyo.Constraint(expr = 3*model.x[1] + 4*model.x[2] <= 100)

opt = pyo.SolverFactory('glpk')
opt.solve(model)
model.display()
