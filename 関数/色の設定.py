#Input
#landingSurface_list, List Access, Surface
#sloperoof_index_list, List Access, int
#takeroof_index_list, List Access, int
#goalroof_list, List Access, int

#Output
#color_list, List, 


import ghpythonlib.components as ghcomp

#色の設定
takeroof_cou = len(takeroof_index_list)
dic = {}
for num, val in enumerate(takeroof_index_list):
    h, s, v = num / takeroof_cou, 1, 1
    takeroof_color = ghcomp.ColourHSV(1, h, s, v)
    dic[val] = takeroof_color

#行方不明の色の設定
missing_color = ghcomp.ColourHSV(1, 0, 0, 0)
dic[-1] = missing_color

#空の色のリストの作成
color_list = [None for i in range(len(landingSurface_list))]

#色の設定
for num2, val2 in enumerate(goalroof_list):
    color = dic[val2]
    color_list[num2] = color

for val3 in takeroof_index_list:
    color3 = dic[val3]
    color_list[val3] = color3
