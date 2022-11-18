#Input
#normal_vec, Item Access, Vector3D

#Output
#a, Vector3D


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

a = FlowVector(normal_vec)
