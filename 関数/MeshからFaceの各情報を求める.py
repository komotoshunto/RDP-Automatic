#Input
#mesh, Item Access, Mesh

#Output
#surface, 
#centroid, 重心
#area, 面積



#Meshの各FaceをSurface, 重心, 面積を返す関数
def SurfaceFromMesh(mesh):
    surface_list = []
    centroid_list = []
    area_list = []
    edges = ghcomp.FaceBoundaries(mesh)
    if isinstance(edges, list):
        for edge in edges:
            explode = ghcomp.Explode(edge, True)
            segment = explode[0]
            if len(segment) == 4:
                surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2], segment[3])
                
            elif len(segment) == 3:
                surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2])
            surface_list.append(surface)
            area = ghcomp.Area(surface)
            area_list.append(area[0])
            centroid_list.append(area[1])
    else:
        explode = ghcomp.Explode(edges, True)
        segment = explode[0]
        if len(segment) == 4:
            surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2], segment[3])
        elif len(segment) == 3:
            surface = ghcomp.EdgeSurface(segment[0], segment[1], segment[2])
        surface_list.append(surface)
        area = ghcomp.Area(surface)
        area_list.append(area[0])
        centroid_list.append(area[1])
    return surface_list, centroid_list, area_list


surface_list, centroid_list, area_list  = SurfaceFromMesh(mesh)
for i in range(len(surface_list)):
    surface.append(surface_list[i])
    centroid.append(centroid_list[i])
    area.append(area_list[i])
