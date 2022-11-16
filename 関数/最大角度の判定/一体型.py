#最も雨の当たる面が多い角度を求める
#建物に振る雨の角度がすべて同じと考えた場合

#Input
#Roof_list, List Access, Mesh
#rain_angle, Item Access, int
#barrier, List Access, Brep

#Output
#a, mesh(サーフェスに分解されている)
#centroid, 法線方向に0.1mmずれた重心点
#vec, 最も雨の当たる面が多い角度
#bool_list, 雨が当たる点(centroid)のboolのリスト


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp
import math


#各角度を定義する
max_angle = rain_angle
min_angel = 0
vec_list = []
step = 10
axis1 = rg.Vector3d(0.0, 1.0, 0.0)
axis2 = rg.Vector3d(0.0, 0.0, 1.0)
for i in range(min_angel, max_angle + 1, step):
    for k in range(0, 360, 30):
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


#Meshの中心点を求める関数
def Mesh_center(mesh):
    centroid = []
    meshfacelist = mesh.Faces
    for num, val in enumerate(meshfacelist):
        center = rg.Collections.MeshFaceList.GetFaceCenter(meshfacelist, num)
        centroid.append(center)
    return centroid


#照射点をmeshから法線方向にずらす
def MovePoint(normal_unit, length, point):
    normal = normal_unit * length
    transform = rg.Transform.Translation(normal)
    rg.Point3d.Transform(point, transform)
    return point
#ずらす長さ
length = 0.1
def NormalOffset_FromMesh(mesh):
    point_list = []
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


#点群から最も雨の当たる角度を求める
def max_RainAngle(centroid_list, barrier):
    ans_cou = float("inf")
    bool_list = []    
    ans_collision = []
    for vec in vec_list:
        projectpoint = ghcomp.ProjectPoint(centroid_list, vec, barrier)
        #ぶつかるものがなかった場合
        if projectpoint[0] == None:
            ans_vec = vec
            print("error")
            if isinstance(projectpoint[1], list):
                ans_collision = projectpoint[1]
            else:
                ans_collision = [projectpoint[1]]
            break
        #ぶつかるものがあった場合
        else:
            cou = len(projectpoint[0])
            if ans_cou > cou:
                ans_cou = cou
                ans_vec = vec
                ans_collision = projectpoint[1]
    
    
    #ぶつかったインデックスのリストをBoolのリストに変換する
    for i in ans_collision:
        if i == -1:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return ans_vec, bool_list


#
centroid_list = []
for i in Roof_list:
    centroid = NormalOffset_FromMesh(i)
    for k in centroid:
        centroid_list.append(k)


vec, bool_list = max_RainAngle(centroid_list, barrier)
