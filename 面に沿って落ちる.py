#Input
#brep_list, List Access, Brep
#face_normal_vec, List Access, Vector3d

#Output
#mesh_list, mesh
#surface, meshのfaceをsurfaceにしたもの
#centroid, meshのfaceの重心
#area, meshのfaceの面積
#locus_list, 重心から流れる軌跡


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp


#法線方向から面を流れる方向を求める関数
def FlowVector(normal_vec):
    x = normal_vec[0]
    y = normal_vec[1]
    if normal_vec[2] == 0:
        z = -1
    else:
        z = -(x**2 + y**2) / normal_vec[2]
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




mesh_list = []
surface = []
centroid = []
area = []
locus_list = []


Landingsurface_list = []
pop_index_list = []
for brep_num0, brep0 in enumerate(brep_list):
    mesh = MeshFromSurface(brep0, 1500)
    surfaces, dummy1, dummy2  = SurfaceFromMesh(mesh)
    for sur in surfaces:
        Landingsurface_list.append(sur)
        pop_index_list.append(brep_num0)


#brepのタイプはBrepであるが、実際には単一面なのでsurface。
for brep_num, brep in enumerate(brep_list):
    normal_vec = face_normal_vec[brep_num]
    
    #barriers：そのsurfaceの障壁
    barriers = BarrierFromBrep(brep, normal_vec)
    
    
    #一時的にリストから削除して元に戻す(削除)
    #pop_index_listと同じ数字をlistから削除する
    val = brep_num
    pop_list = [i for i, x in enumerate(pop_index_list) if x == val]
    add_list = []
    for add_num in sorted(pop_list, reverse=False):
        add = Landingsurface_list[add_num]
        add_list.append(add)
    for pop_num in sorted(pop_list, reverse=True):
        Landingsurface_list.pop(pop_num)
    
    
    #centroid：そのsurface上にある点群(点群はmesh化した重点)
    mesh = MeshFromSurface(brep, 1500)
    mesh_list.append(mesh[0])
    surfaces, centroids, areas  = SurfaceFromMesh(mesh)
    for face_num in range(len(surfaces)):
        surface.append(surfaces[face_num])
        centroid.append(centroids[face_num])
        area.append(areas[face_num])
        descent_point = DescentPoint(centroids[face_num], normal_vec, barriers)
        
        
        projectpoint = ghcomp.ProjectPoint(descent_point, rg.Vector3d(0, 0, -1), Landingsurface_list)
        if projectpoint[1] != -1:
            locus_end_point = projectpoint[0]
        else:
            locus_end_point = rg.Point3d(descent_point[0], descent_point[1], descent_point[2] - 1000)
        locus_points = [centroids[face_num], descent_point, locus_end_point]
        locus = rg.Polyline(locus_points)
        locus_list.append(locus)

    
    
    #一時的にリストから削除して元に戻す(復元)
    for restore_num, restore_vel in enumerate(sorted(pop_list, reverse=False)):
        Landingsurface_list.insert(restore_vel, add_list[restore_num])
