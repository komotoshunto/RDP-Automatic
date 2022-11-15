#Input
#brep, List Access, Brep

#Output
#a, mesh(サーフェスに分解されている)


import Rhino.Geometry as rg

a = []
param = rg.MeshingParameters()
param.MaximumEdgeLength = len
param.MinimumEdgeLength = len
param.JaggedSeams = True
for i in brep:
    facelist = i.Faces
    for face in facelist:
        mesh = rg.Mesh.CreateFromSurface(face, param)
        a.append(mesh)
