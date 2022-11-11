#Input
#x, Item Access, Brep

#Output
#a, 各面積

import Rhino.Geometry as rg

a = []
sur = x.Faces
for i in sur:
    areamass = rg.AreaMassProperties.Compute(i)
    print(areamass)
    result = areamass.Area
    a.append(result)
