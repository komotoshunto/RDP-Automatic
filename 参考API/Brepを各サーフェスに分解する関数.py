#Input
#x, List Access, Brep

#Output
#a, サーフェスのリスト

a = []
for i in x:
    face = i.Faces
    for k in face:
        print(k)
        a.append(k)
