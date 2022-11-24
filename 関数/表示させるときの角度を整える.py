#Input
#x, List Access, Surface

#Output
#normal_list, 
#flame_list,


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math


def TextVisible_flame(normal, origin):
    if normal[2] == 1 or normal[2] == -1:
        flame_x = rg.Vector3d(1, 0, 0)
        flame_y = rg.Vector3d(0, 1, 0)
        base_vec = rg.Vector3d(0, 0, 1)
    else:
        base_vec = rg.Vector3d(normal[0], normal[1], 0)
        flame_x = rs.VectorRotate(base_vec, 90, rg.Vector3d(0, 0, 1))
        flame_y = rs.VectorRotate(normal, -90, flame_x)
    flame = rg.Plane(origin, flame_x, flame_y)
    return flame


flame_list = []
for surface in x:
    param = (0.5, 0.5)
    surface_param = rs.SurfaceParameter(surface, param)
    u = surface_param[0]
    v = surface_param[1]
    normal = rg.Surface.NormalAt(surface, u, v)
    point = rg.Surface.PointAt(surface, u, v)
    flame = TextVisible_flame(normal, point)
    flame_list.append(flame)
