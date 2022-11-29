import itertools as it
slope_roof = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
slope_roof_area = [356, 332, 271, 131, 158, 428, 292, 201, 315, 260, 420, 168, 158, 364, 333, 248, 873, 543, 54, 544]

take_roof = [100, 200, 300]
take_roof_area = [376, 325, 324]

#隣接関係
adjacency = [[1, 8], [2, 9], [3, 9],[4, 10],[5, 10],[6, 11],[7, 12],[8, 13],[9, 100],[10, 14],[11, 15],[12, 7],[13, 100],[14, 200],[15, 300],[16, 300], [18, 17], [17, -1], [19, 20], [20, 19]]

#-----------------------------------------------------------------------------------------------------------------------------
def RainFlow_judge(adjacency, slope_roof, slope_roof_area, take_roof, take_roof_area):
    #どの屋根にも落ちない屋根を追加する
    take_roof.append(-1)
    take_roof_area.append(0)

    search_take_roof_list = [[i] for i in take_roof]

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
    
    loop_list = tuple(it.chain.from_iterable(adjacency))

    goalroof_list = []
    for val3 in slope_roof:
        cou = 0
        for num4, val4 in enumerate(search_take_roof_list):
            if val3 in val4:
                take_roof_indexl = take_roof[num4]
                goalroof_list.append(take_roof_indexl)
                break
            elif val3 in loop_list:
                goalroof_list.append(None)
                break
            else:
                cou += 1
    return goalroof_list, take_roof_area


goalroof_list, take_roof_area = RainFlow_judge(adjacency, slope_roof, slope_roof_area, take_roof, take_roof_area)
print(goalroof_list)
print(take_roof_area)

#-----------------------------------------------------------------------------------------------------------------------------
#[100, 100, 100, 200, 200, 300, None, 100, 100, 200, 300, None, 100, 200, 300, 300, -1, -1, None, None]
#[2009, 1238, 1753, 1416]



dic_list = []
for num, val in enumerate(goalroof_list):
    dic = {}
    dic["start"] = slope_roof[num]
    dic["goal"] = val
    dic_list.append(dic)

print(dic_list)
#[{'start': 1, 'goal': 100}, {'start': 2, 'goal': 100}, {'start': 3, 'goal': 100}, {'start': 4, 'goal': 200}, {'start': 5, 'goal': 200}, {'start': 6, 'goal': 300}, {'start': 7, 'goal': None}, {'start': 8, 'goal': 100}, {'start': 9, 'goal': 100}, {'start': 10, 'goal': 200}, {'start': 11, 'goal': 300}, {'start': 12, 'goal': None}, {'start': 13, 'goal': 100}, {'start': 14, 'goal': 200}, {'start': 15, 'goal': 300}, {'start': 16, 'goal': 300}, {'start': 17, 'goal': -1}, {'start': 18, 'goal': -1}, {'start': 19, 'goal': None}, {'start': 20, 'goal': None}]
