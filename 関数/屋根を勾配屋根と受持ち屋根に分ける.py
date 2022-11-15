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
import ghpythonlib.components as ghcomp
import math

#屋根を勾配屋根と受持ち屋根に分ける
#-1: 雨が当たらない, 0: 受持ち屋根, 1: 勾配屋根
def roof_judge(surface, rain_angle):
    judge_angle = math.cos(math.radians(180 - rain_angle))
    normal = rg.Surface.NormalAt(surface, 0.5, 0.5)
    z = round(normal[2], 5) + 0.0
    print(z)
    if z == 1:
        judge = 0
    elif z <= judge_angle and z != 1:
        judge = -1
    else:
        judge = 1
    return judge



ChargeRoof_list = []
SlopeRoof_list = []
NonRoof_list = []
for i in geometry:
    facelist = i.Faces
    for k in facelist:
        judge = roof_judge(k, rain_angle)
        if judge == 0:
            ChargeRoof_list.append(k)
        elif judge == 1:
            SlopeRoof_list.append(k)
        elif judge == -1:
            NonRoof_list.append(k)
