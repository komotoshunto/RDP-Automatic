#Input
#mesh_list, List Access, Mesh

#Output
#a, そのメッシュにあるFaceの法線リスト

#問題点
#メッシュ同士が結合された状態では、「mesh.FaceNormals」の部分が何も返されず、Noneになる。

import Rhino.Geometry as rg

a = []
for mesh in mesh_list:
    normal_list = mesh.FaceNormals
    for normal in normal_list:
        a.append(normal)
