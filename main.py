# make sure the following packages are installed
# 1. openopt
# 2. FuncDesigner

from Objective      import ObjectiveMain
from Constraints    import Constraint1, Constraint2
from Coordinator    import GaussSeidelCoordinator
from openopt        import NLP
import coupling     # to access global variables: y1, y2


# initial value of design variables
x1 = 1
z1 = 5
z2 = 2
x0 = [x1, z1, z2]

# calculate the constraints first
[y1, y2, _] = GaussSeidelCoordinator(x1, z1, z2, 0) # find values of y1, y2 that is consistent with x1, z1, z2
coupling.y1 = y1
coupling.y2 = y2


# print initial values
print('Initial Objective: ' + str(ObjectiveMain(x0)))
print('[x1 z1 z2] = '       + str(x0))
print('[y1 y2] = ['         + str(coupling.y1) + ', ' + str(coupling.y2) +']')

# Non linear Programming for optimizing the Sellar problem
# documentation at: https://github.com/troyshu/openopt/blob/master/openopt/oo.py
p = NLP(f = ObjectiveMain, x0 = x0, lb = (0, -10, 0), ub = (10, 10, 10), c = [Constraint1, Constraint2], iprint = 50)
res = p.solve('scipy_cobyla')


# print the results
print('\n' + '-'*50)
print('Final Objective: ' + str(res.ff))
print('[x1 z1 z2] = '     + str(res.xf))
print('[y1 y2] = ['       + str(coupling.y1) + ', ' + str(coupling.y2) +']')