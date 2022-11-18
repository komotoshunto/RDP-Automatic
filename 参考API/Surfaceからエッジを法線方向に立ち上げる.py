#Input
#surface_list, List Access, Brep
#face_normal_vec, List Access, Vector3d

#Output
#AnswerVector_list, 


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp


edge_barrier_list = []
for num, surface in enumerate(surface_list):
    barrier_list = []
    edges = surface.Edges
    for edge in edges:
        #「barrier」がそのサーフェス単体の障壁
        barrier = rg.Surface.CreateExtrusion(edge, face_normal_vec[num] * 100)
        edge_barrier_list.append(barrier)
