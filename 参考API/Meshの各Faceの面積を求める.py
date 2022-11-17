#Input
#mesh_list, List Access, Mesh

#Output
#a, Faceの面積

import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp


a = []
for i in mesh_list:
    result1 = ghcomp.FaceBoundaries(i)
    if isinstance(result1, list):
        for k in result1:
            result2 = rg.AreaMassProperties.Compute(k)
            area = result2.Area
            a.append(area)
    else:
        result2 = rg.AreaMassProperties.Compute(k)
        area = result2.Area
        a.append(area)
