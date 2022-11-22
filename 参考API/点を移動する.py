#Input
#x, Item Access, Point3d

#Output
#a, point


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#ProjectPointに引っかからないように照射点をmeshから法線方向にずらす
def MovePoint(point, vector, length):
    rg.Vector3d.Unitize(vector)
    normal = vector * length
    transform = rg.Transform.Translation(normal)
    rg.Point3d.Transform(point, transform)
    return point

a = MovePoint(x, rg.Vector3d(0, 5, 1), 1)
