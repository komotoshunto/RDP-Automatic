slope_roof = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
slope_roof_area = [356, 332, 271, 131, 158, 428, 292, 201, 315, 260, 420, 168, 158, 364, 333, 248, 873, 543, 54, 544]

take_roof = [100, 200, 300]
take_roof_area = [376, 325, 324]

#隣接関係
adjacency = [[1, 8], [2, 9], [3, 9],[4, 10],[5, 10],[6, 11],[7, 12],[8, 13],[9, 100],[10, 14],[11, 15],[12, 7],[13, 100],[14, 200],[15, 300],[16, 300], [18, 17], [17, -1], [19, 20], [20, 19]]



def RainFlow_judge(slope_roof, slope_roof_area, take_roof, take_roof_area):
    #どの屋根にも落ちない屋根を追加する
    take_roof.append(-1)
    take_roof_area.append(0)

    search_take_roof_list = [[i] for i in take_roof]
    #search_take_roof_list:[[100], [200], [300], [-1]]

    while len(adjacency) > 0:
        pop_list = []
        judge = len(adjacency)
        for num1, val1 in enumerate(adjacency):
            target = val1[1]
            adjacent = val1[0]
            for num2, val2 in enumerate(search_take_roof_list):
                if target in val2:
                    search_take_roof_list[num2].append(adjacent)
                    pop_list.append(num1)
                    a = slope_roof.index(adjacent)
                    area = slope_roof_area[a]
                    take_roof_area[num2] += area
                    break
        for j in sorted(pop_list, reverse=True):
            adjacency.pop(j)    
        if len(adjacency) == judge:
            break
    return search_take_roof_list, take_roof_area


search_take_roof_list, take_roof_area = RainFlow_judge(slope_roof, slope_roof_area, take_roof, take_roof_area)


print("search_take_roof_list", search_take_roof_list)
print("adjacency", adjacency)
print("take_roof_area", take_roof_area)



#-------------------------------------------------------------------------------------------

#search_take_roof_list [[100, 9, 13, 2, 3, 8, 1], [200, 14, 10, 4, 5], [300, 15, 16, 11, 6], [-1, 17, 18]]
#adjacency [[7, 12], [12, 7], [19, 20], [20, 19]]
#take_roof_area [2009, 1238, 1753, 1416]
