#Output
#a, point


import Rhino.Geometry as rg

a = rg.Point3d(0, 100, 0)
vec = rg.Vector3d(0, 0, 100)
transform = rg.Transform.Translation(vec)
#指定した点（a）が変化するので、別の変数に代入できない
rg.Point3d.Transform(a, transform)

