id_list = [23, 54, 56, 98]
vector = [(0, 3, 5), (4, -3, -6), (-3, 7, -2), (4, 8, 2)]


#辞書型リストの作成
list_dic = []
for num, val in enumerate(id_list):
    dic = {}
    dic["id"] = val
    dic["vector"] = vector[num]
    list_dic.append(dic)
print(list_dic)
#[{'id': 23, 'vector': (0, 3, 5)}, {'id': 54, 'vector': (4, -3, -6)}, {'id': 56, 'vector': (-3, 7, -2)}, {'id': 98, 'vector': (4, 8, 2)}]


#要素の取り出し
for k in list_dic:
    key = "vector"
    val = k[key]
    print(val)
