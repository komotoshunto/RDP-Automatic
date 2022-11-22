import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp


#PointをVector方向へ指定の長さ分ずらす
def MovePoint(point, vector, length):
    rg.Vector3d.Unitize(vector)
    normal = vector * length
    transform = rg.Transform.Translation(normal)
    rg.Point3d.Transform(point, transform)
    return point


#屋根面を伝って、降下するpointを返す関数
def DescentPoint(center, normal_vec, barriers):
    flow_vec = FlowVector(normal_vec)
    projectpoint = ghcomp.ProjectPoint(center, flow_vec, barriers)
    point = projectpoint[0]
    return point


#雨の到着地点とその軌跡を返す関数
#point, Item Access, Point3d, 雨が流れるスタート地点
#normal_vec, Item Access, Vector3d, スタート地点の法線
#barriers, List Access, Surface, その屋根のエッジから法線方向に立ち上げたもの
#LandingSurface_list, List Access, Geometry
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


