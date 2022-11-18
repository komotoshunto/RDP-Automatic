#Input
#mesh_list, List Access, Mesh

#Output
#a, 法線ベクトルのリスト


import ghpythonlib.components as ghcomp

a = []
for mesh in mesh_list:
    faceN = ghcomp.FaceNormals(mesh)
    if isinstance(faceN[1], list):
        normal_list = faceN[1]
        for normal in normal_list:
            a.append(normal)
    else:
        normal = faceN[1]
        a.append(normal)
