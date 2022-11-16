#Input
#x, Item Access, Brep

#Output
#a, 各重心

import Rhino.Geometry as rg

a = []
sur = x.Faces
for i in sur:
    result = rg.Surface.NormalAt(i, 0.5, 0.5)
    a.append(result)
