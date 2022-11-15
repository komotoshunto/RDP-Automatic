import Rhino.Geometry as rg

a1 = rg.Point3d(0, 0, 0)
a2 = rg.Point3d(0, 50, 100)
a = rg.Point3d.DistanceTo(a1, a2)
print(a)
