#testcode.pyを使用する
#--------------------------------------------------------------

slope_roof = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
slope_roof_area = [356, 332, 271, 131, 158, 428, 292, 201, 315, 260, 420, 168, 158, 364, 333, 248]

take_roof = [17, 18, 19]
take_roof_area = [376, 325, 324]


#隣接関係
adjacency = [[1, 8], [2, 9], [3, 9],[4, 10],[5, 10],[6, 11],[7, 12],[8, 13],[9, 17],[10, 14],[11, 15],[12, 15],[13, 17],[14, 18],[15, 19],[16, 19]]
search_take_roof_list = [[i] for i in take_roof]
print("search_take_roof_list", search_take_roof_list)

Total_area = take_roof_area
while len(adjacency) > 0:
    pop_list = []
    for num1, i in enumerate(adjacency):
        target = i[1]
        adjacent = i[0]
        for num2, k in enumerate(search_take_roof_list):
            if target in k:
                search_take_roof_list[num2].append(adjacent)
                pop_list.append(num1)
                a = slope_roof.index(adjacent)
                area = slope_roof_area[a]
                Total_area[num2] += area
                break
    for j in sorted(pop_list, reverse=True):
        adjacency.pop(j)


print("search_take_roof_list", search_take_roof_list)
print("adjacency", adjacency)
print("Total_area", Total_area)

#-------------------------------------------------------------------------------------------
#search_take_roof_list [[17], [18], [19]]

#search_take_roof_list [[17, 9, 13, 2, 3, 8, 1], [18, 14, 10, 4, 5], [19, 15, 16, 11, 12, 6, 7]]
#adjacency []
#Total_area [2009, 1238, 2213]
