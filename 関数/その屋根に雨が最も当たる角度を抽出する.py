#Input
#rain_angle, Item Access, float
#mesh_list, List Access, Mesh

#Output
#AnswerVector_list, 


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp
import math


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
            vec = rg.Vector3d(0.0, 0.0, 1.0)
            vec_list.append(vec)
            break
        else:
            angleRad1 = math.radians(i)
            angleRad2 = math.radians(k)
            vec = rg.Vector3d(0.0, 0.0, 1.0)
            re_vec1 = rg.Vector3d.Rotate(vec, angleRad1, axis1)
            re_vec2 = rg.Vector3d.Rotate(vec, angleRad2, axis2)
            vec_list.append(vec)

AnswerVector_list = []
#重心を求める
for num, mesh in enumerate(mesh_list):
    meshfacelist = mesh.Faces
    centroid = []
    for h in range(len(meshfacelist)):
        center = rg.Collections.MeshFaceList.GetFaceCenter(meshfacelist, h)
        centroid.append(center)
    
    #ProjectPointに引っかからないように照射点と同じ位置にあるmeshを削除する
    add = mesh
    mesh_list.pop(num)
    
    ans_cou = float("inf")
    for vec in vec_list:
        projectpoint = ghcomp.ProjectPoint(centroid, vec, mesh_list)
        if projectpoint[0] == None:
            count = 0
            ans_vec = vec
            break
        else:
            count = len(projectpoint[0])
            cou = count
            if cou < ans_cou:
                ans_cou = cou
                ans_vec = vec
    AnswerVector_list.append(ans_vec)
    
    #消したmeshを元に戻す
    mesh_list.insert(num, add)
