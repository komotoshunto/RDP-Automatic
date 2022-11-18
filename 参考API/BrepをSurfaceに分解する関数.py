#Input
#brep_list, List Access, Brep

#Output
#a, サーフェスのリスト

surface_list = []
for brep in brep_list:
    faces = brep.Faces
    for face in faces:
        surface_list.append(face)
