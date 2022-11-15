#testcode.pyを使用する
#--------------------------------------------------------------

search_take_roof_list = [[i] for i in take_roof]

#隣接関係
adjacency = [[1, 8], [2, 9], [3, 9],[4, 10],[5, 10],[6, 11],[7, 12],[8, 13],[9, 17],[10, 14],[11, 15],[12, 15],[13, 17],[14, 18],[15, 19],[16, 19]]
search_take_roof_list = [[i] for i in take_roof]
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

print(search_take_roof_list)
print(adjacency)
print(Total_area)



#-------------------------------------------------------------------------------------------
#[[17, 9, 13, 2, 3, 8, 1], [18, 14, 10, 4, 5], [19, 15, 16, 11, 12, 6, 7]]
#[]
#[3642, 2151, 4102]
