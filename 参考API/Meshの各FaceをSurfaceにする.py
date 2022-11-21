#Input
#mesh, Item Access, Mesh

#Output
#a, surfaceのリスト


import ghpythonlib.components as ghcomp
import Rhino.Geometry as rg


#Meshの各FaceをSurfaceにする関数
def SurfaceFromMesh(mesh):
    surface_list = []
    edges = ghcomp.FaceBoundaries(mesh)
    for edge in edges:
        explode = ghcomp.Explode(edge, True)
        segment = explode[0]
        if len(segment) == 4:
            surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2], segment[3])
        elif len(segment) == 3:
            surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2])
        surface_list.append(surface)

a = SurfaceFromMesh(mesh)
