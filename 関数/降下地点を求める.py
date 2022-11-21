#Input
#center, Item Access, Point3d
#normal_vec, Item Access, Vector3d
#barriers, List Access, Brep

#Output
#a, 降下地点


#屋根面を伝って降下するpointを返す関数
def DescentPoint(center, normal_vec, barriers):
    flow_vec = FlowVector(normal_vec)
    projectpoint = ghcomp.ProjectPoint(center, flow_vec, barriers)
    point = projectpoint[0]
    return point

a = DescentPoint(center, normal_vec, barriers)
