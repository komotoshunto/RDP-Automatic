#Input
#rain_angle, Item Access, float
#roof, List Access, Brep

#Output
#a, 係数

#屋根の面積に係数をかける


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

#壁の角度から雨の受ける量の係数を求める関数
#rain_angle(垂直に落ちる：0, 日本設計最大入射角：30)
def rain_area_adju(normal_vec, rain_angle):
    z = normal_vec[2]    
    wall_angle = round(math.degrees(math.acos(z)), 5)
    max_wall_angle = 90 + rain_angle
    if wall_angle >= 0 and wall_angle < rain_angle:
        k = 1
    elif wall_angle < max_wall_angle and wall_angle >= rain_angle:
        result = math.sin(math.radians(90 - wall_angle + rain_angle))
        k = round(result, 5)
    elif wall_angle >= max_wall_angle:
        k = 0
    return k

a = []
for k in roof:
    brepface = k.Faces
    normal_vec = rg.Surface.NormalAt(brepface[0], 0.5, 0.5)
    k = rain_area_adju(normal_vec, rain_angle)
    a.append(k)
