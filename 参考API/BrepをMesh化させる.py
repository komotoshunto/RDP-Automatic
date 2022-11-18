#Input
#brep, List Access, Brep

#Output
#a, mesh(サーフェスに分解されている)


import Rhino.Geometry as rg

#Brepをmesh化させる
def MeshFromBrep(brep, edge_length):
    mesh_list = []
    param = rg.MeshingParameters()
    param.MaximumEdgeLength = edge_length
    param.MinimumEdgeLength = edge_length
    param.JaggedSeams = True
    for i in brep:
        facelist = i.Faces
        for face in facelist:
            mesh = rg.Mesh.CreateFromSurface(face, param)
            mesh_list.append(mesh)
    return mesh_list

a = MeshFromBrep(geometry, 1500)
