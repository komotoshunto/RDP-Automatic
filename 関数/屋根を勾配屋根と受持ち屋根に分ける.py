#Input
#geo, List Access, Brep, 
#angle, Item Access, float, 

#Output
#face_list, 
#charge_roof, 
#slope_roof, 
#non_roof, 


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

face_list = []
normal_vec = []
charge_roof = []
slope_roof = []
non_roof = []

judge_angle = math.cos(math.radians(180 - angle))
for i in geo:
    face = i.Faces
    for k in face:
        face_list.append(k)
        normal = rg.Surface.NormalAt(k, 0.5, 0.5)
        normal_vec.append(normal)
        z = round(normal[2], 5) + 0.0
        if z == 1:
            charge_roof.append(k)
        elif z < judge_angle:
            non_roof.append(k)
        else:
            slope_roof.append(k)
