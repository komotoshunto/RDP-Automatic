#Input
#mesh_list, List Access, Mesh

#Output
#centroid, 各重心


import Rhino.Geometry as rg

#Meshの中心点を求める関数
def Mesh_center(mesh_list):
    centroid = []
    for mesh in mesh_list:
        meshfacelist = mesh.Faces
        for num, val in enumerate(meshfacelist):
            center = rg.Collections.MeshFaceList.GetFaceCenter(meshfacelist, num)
            centroid.append(center)
    return centroid

centroid = Mesh_center(mesh_list)
