#Input
#point, List Access, Point
#barrier, List Access, Geometry

#Output
#a, 照射された点。(障壁にぶつかっていなくてもlineの長さの限界が返されるのでNoneはない)
#b, 照射された点までの距離
#c, ぶつかった障壁のインデックス。（ぶつからなかったら-1を返す）
#count, 障壁にぶつからなかった個数


import Rhino.Geometry as rg
import ghpythonlib.components as ghcomp

vec = rg.Vector3d(0, 0, -1)
line_list = []
for i in point:
    line = rg.Line(i, vec)
    line_list.append(line)
result = ghcomp.IsoVistRay(line_list, 100000, barrier)
a = result[0]
b = result[1]
c = result[2]
count = c.count(-1)
