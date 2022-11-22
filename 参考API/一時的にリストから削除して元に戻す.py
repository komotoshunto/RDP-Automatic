list = [430, 10, 53, 43, 4, 50]
pop_index_list = [1, 2, 1, 1, 2, 2]
print("削除前", list)


val = 1 #pop_index_listと同じ数字をlistから削除する
pop_list = [i for i, x in enumerate(pop_index_list) if x == val]
add_list = []
for add_num in sorted(pop_list, reverse=False):
    add = list[add_num]
    add_list.append(result)


for pop_num in sorted(pop_list, reverse=True):
    list.pop(pop_num)
print("削除後", list)


for restore_num, restore_val in enumerate(sorted(pop_list, reverse=False)):
    list.insert(restore_val, add_list[restore_val])
print("修正後", list)
