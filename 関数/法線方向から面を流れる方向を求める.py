#Input
#normal_vec, Item Access, Vector3D

#Output
#a, Vector3D


#法線方向から面を流れる方向を求める関数
def FlowVector(normal_vec):
    print(normal_vec[2])
    if normal_vec[2] == 0:
        z = -1
    else:
        z = -1 * ((normal_vec[0]**2 + normal_vec[1]**2)**(1/2))
    k = (-1) * ((normal_vec[2] * z) / (normal_vec[0]**2 + normal_vec[1]**2))
    x = normal_vec[0] * k
    y = normal_vec[1] * k
    flow_vec = rg.Vector3d(x, y, z)
    return flow_vec

a = FlowVector(normal_vec)
