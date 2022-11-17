#Input
#mesh_list, List Access, Mesh

#Output
#a, そのメッシュにあるFaceの法線リスト


import Rhino.Geometry as rg

a = []
for mesh in mesh_list:
    normal_list = mesh.FaceNormals
    for normal in normal_list:
        a.append(normal)
