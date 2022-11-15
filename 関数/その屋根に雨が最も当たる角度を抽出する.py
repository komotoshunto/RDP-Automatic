#Input
#angle_rainfall, Item Access, float
#roof_list, List Access, Mesh
#barrier, List Access, GeometryBese


#Output
#ans_vec, 
#intersect_list, 


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math
import System
import Grasshopper.Kernel.Data.GH_Path as gh_path
import Grasshopper.DataTree as datatree

#各角度を定義する
max_angle = int(rain_angle)
min_angel = 0
vec_list = []
step = 10
axis1 = rg.Vector3d(0.0, 1.0, 0.0)
axis2 = rg.Vector3d(0.0, 0.0, 1.0)
for i in range(min_angel, max_angle + 1, step):
    for k in range(0, 360, step):
        if i == 0:
            break
        else:
            angleRad1 = math.radians(i)
            angleRad2 = math.radians(k)
            vec = rg.Vector3d(0.0, 0.0, 1.0)
            re_vec1 = rg.Vector3d.Rotate(vec, angleRad1, axis1)
            re_vec2 = rg.Vector3d.Rotate(vec, angleRad2, axis2)
            vec_list.append(vec)
def max_projected_area(mesh, barrier):
    #重心を求める
    centroid = []
    mfl = mesh.Faces
    for h in range(len(mfl)):
        center = rg.Collections.MeshFaceList.GetFaceCenter(mfl, h)
        centroid.append(center)
    
    #光線を発射
    ans_count = float("inf")
    for dir in vec_list:
        count = 0
        intersect = []
        for point in centroid:
            ray = rg.Ray3d(point, dir)
            rayshootevent = rg.Intersect.Intersection.RayShoot(barrier, ray, 1)
            count += len(rayshootevent)
            if len(rayshootevent) == 0:
                intersect.append(True)
            else:
                intersect.append(False)
        if count < ans_count:
            ans_count = count
            ans_vec = dir
            intersect_list = intersect
    
    return intersect_list, ans_vec


tree1 = datatree[System.Object]()
tree2 = datatree[System.Object]()
for num, roof in enumerate(roof_list):
    intersect, vec = max_projected_area(roof, barrier)
    print(num, intersect)
    path = gh_path(num)
    tree1.Add(vec, path)
    tree2.Add(intersect, path)
ans_vec = tree1
intersect_list = tree2
