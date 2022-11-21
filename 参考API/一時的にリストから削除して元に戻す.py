list = [430, 10, 53, 43, 4, 50]
pop_index_list = [1, 2, 1, 1, 2, 2]


val = 1 #pop_index_listと同じ数字をlistから削除する
pop_list = [i for i, x in enumerate(pop_index_list) if x == val]
print("削除前", list)


add = []
for k in sorted(pop_list, reverse=False):
    result = list[k]
    add.append(result)



for i in sorted(pop_list, reverse=True):
    list.pop(i)
print("削除後", list)



for num, j in enumerate(sorted(pop_list, reverse=False)):
    list.insert(j, add[num])
print("修正後", list)
