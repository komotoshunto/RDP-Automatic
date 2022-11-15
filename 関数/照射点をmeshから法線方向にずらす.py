#Input
#mesh_list, List Access, Mesh

#Output
#a, ずれた点群

import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp

#ProjectPointに引っかからないように照射点をmeshから法線方向にずらす
def MovePoint(normal_unit, length, point):
    normal = normal_unit * length
    transform = rg.Transform.Translation(normal)
    rg.Point3d.Transform(point, transform)
    return point
#ずらす長さ
length = 0.1
def NormalOffset_FromMesh(mesh_list):
    point_list = []
    for num, mesh in enumerate(mesh_list):
        result = ghcomp.FaceNormals(mesh)
        points = result[0]
        if isinstance(points, list):
            for num in range(len(points)):
                point = points[num]
                normal_unit = result[1][num]
                point = MovePoint(normal_unit, length, point)
                point_list.append(point)
        else:
            point = points
            normal_unit = result[1]
            point = MovePoint(normal_unit, length, point)
            point_list.append(point)
    return point_list

a = NormalOffset_FromMesh(mesh_list)
