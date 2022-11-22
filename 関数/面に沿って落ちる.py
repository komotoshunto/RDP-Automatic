#Input
#brep_list, List Access, Brep
#Landingsurface_list, List Access, Geometry
#face_normal_vec, List Access, Vector3d

#Output
#mesh_list, mesh
#locus_list, 重心から流れる軌跡


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


mesh_list = []
surface = []
area = []
locus_list = []
locus_points_list = []


#brepのタイプはBrepであるが、実際には単一面なのでsurface。
for brep_num, brep in enumerate(brep_list):
    normal_vec = face_normal_vec[brep_num]
    
    #barriers：そのsurfaceの障壁
    barriers = BarrierFromBrep(brep, normal_vec)
    
    #centroid：そのsurface上にある点群(点群はmesh化した重点)
    mesh = MeshFromSurface(brep, 1500)
    mesh_list.append(mesh[0])
    surfaces, centroids, areas  = SurfaceFromMesh(mesh)
    for face_num in range(len(surfaces)):
        moved_point = MovePoint(centroids[face_num], normal_vec, 0.5)
        surface.append(surfaces[face_num])
        area.append(areas[face_num])
        descent_point = DescentPoint(moved_point, normal_vec, barriers)
        
        projectpoint = ghcomp.ProjectPoint(descent_point, rg.Vector3d(0, 0, -1), Landingsurface_list)
        if projectpoint[1] != -1:
            locus_end_point = projectpoint[0]
        else:
            locus_end_point = rg.Point3d(descent_point[0], descent_point[1], descent_point[2] - 10000)
        locus_points = [moved_point, descent_point, locus_end_point]
        locus = rg.Polyline(locus_points)
        locus_list.append(locus)
