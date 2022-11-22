#Input
#brep_list, List Access, Brep
#Landingsurface_list, List Access, Geometry
#face_normal_vec, List Access, Vector3d

#Output
#surface_list, 各MeshのFaceをSurface化したもの
#area_list, surface_listの面積
#locus_list, 雨の軌跡
#LandingIndex_list, 各Surface化した面の雨が、落ちた先のSurfaceのインデックスを返す
#LandingSurface_list, 


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp


#法線方向から面を流れる方向を求める関数
def FlowVector(normal_vec):
    if normal_vec[2] == 0:
        z = -1
    else:
        z = -1 * ((normal_vec[0]**2 + normal_vec[1]**2)**(1/2))
    k = (-1) * ((normal_vec[2] * z) / (normal_vec[0]**2 + normal_vec[1]**2))
    x = normal_vec[0] * k
    y = normal_vec[1] * k
    flow_vec = rg.Vector3d(x, y, z)
    return flow_vec

#surfaceをmesh化させる
def MeshFromSurface(surface, edge_length):
    mesh_list = []
    param = rg.MeshingParameters()
    param.MaximumEdgeLength = edge_length
    param.MinimumEdgeLength = edge_length
    param.JaggedSeams = True
    mesh = rg.Mesh.CreateFromBrep(surface, param)
    return mesh

#屋根面を伝って、降下するpointを返す関数
def DescentPoint(center, normal_vec, barriers):
    flow_vec = FlowVector(normal_vec)
    projectpoint = ghcomp.ProjectPoint(center, flow_vec, barriers)
    point = projectpoint[0]
    return point

#Brepから法線方向に障壁を立ち上げる関数
def BarrierFromBrep(Brep, normal_vec):
    edges = Brep.Edges
    barriers = []
    for edge in edges:
        #「barrier」がそのサーフェス単体の障壁
        barrier = rg.Surface.CreateExtrusion(edge, normal_vec)
        barriers.append(barrier)
    return barriers

#PointをVector方向へ指定の長さ分ずらす
def MovePoint(point, vector, length):
    rg.Vector3d.Unitize(vector)
    normal = vector * length
    transform = rg.Transform.Translation(normal)
    rg.Point3d.Transform(point, transform)
    return point

#Meshの各FaceをSurface, 重心, 面積を返す関数
def SurfaceFromMesh(mesh):
    surface_list = []
    centroid_list = []
    area_list = []
    edges = ghcomp.FaceBoundaries(mesh)
    if isinstance(edges, list):
        for edge in edges:
            explode = ghcomp.Explode(edge, True)
            segment = explode[0]
            if len(segment) == 4:
                surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2], segment[3])
                
            elif len(segment) == 3:
                surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2])
            surface_list.append(surface)
            area = ghcomp.Area(surface)
            area_list.append(area[0])
            centroid_list.append(area[1])
    else:
        explode = ghcomp.Explode(edges, True)
        segment = explode[0]
        if len(segment) == 4:
            surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2], segment[3])
        elif len(segment) == 3:
            surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2])
        surface_list.append(surface)
        area = ghcomp.Area(surface)
        area_list.append(area[0])
        centroid_list.append(area[1])
    return surface_list, centroid_list, area_list

#雨の到着地点とその軌跡を返す関数
def RainFlow(point, normal_vec, barriers, LandingSurface_list):
    moved_point = MovePoint(point, normal_vec, 0.5)
    descent_point = DescentPoint(moved_point, normal_vec, barriers)
    projectpoint = ghcomp.ProjectPoint(descent_point, rg.Vector3d(0, 0, -1), LandingSurface_list)
    project_index = projectpoint[1]
    
    #軌跡を表す
    if projectpoint[1] != -1:
        locus_end_point = projectpoint[0]
    else:
        locus_end_point = rg.Point3d(descent_point[0], descent_point[1], descent_point[2] - 1000)
    locus_points = [moved_point, descent_point, locus_end_point]
    locus = rg.Polyline(locus_points)
    return project_index, locus



normal_list = []
barriers_list = []


surface_list = []
area_list = []
centroid_list = []
index_list = []


#brepのタイプはBrepであるが、実際には単一面なのでsurface。
for brep_num, brep in enumerate(slope_roof):
    normal_vec = rs.SurfaceNormal(brep, (0.5, 0.5))
    normal_list.append(normal_vec)
    #barriers：そのsurfaceの障壁
    barriers = BarrierFromBrep(brep, normal_vec)
    barriers_list.append(barriers)
    
    
    #centroid：そのsurface上にある点群(点群はmesh化した重点)
    mesh = MeshFromSurface(brep, 1500)
    surfaces, centroids, areas  = SurfaceFromMesh(mesh)
    for face_num in range(len(surfaces)):
        surface_list.append(surfaces[face_num])
        area_list.append(areas[face_num])
        centroid_list.append(centroids[face_num])
        index_list.append(brep_num)


surface_type = [0 for cou1 in range(len(surface_list))]
charge_roof_type = [1 for cou2 in range(len(charge_roof))]
LandingSurface_type = surface_type + charge_roof_type
LandingSurface_list = surface_list + charge_roof


locus_list = []
LandingIndex_list = []
for num in range(len(LandingSurface_list)):
    if LandingSurface_type[num] == 0:
        centroid = centroid_list[num]
        normal_vec = normal_list[index_list[num]]
        barriers = barriers_list[index_list[num]]
        
        
        project_index, locus = RainFlow(centroid, normal_vec, barriers, LandingSurface_list)
        LandingIndex_list.append(project_index)
        locus_list.append(locus)
    else:
        print(1)        
