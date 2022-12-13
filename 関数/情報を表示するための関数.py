#Rhino上で情報を表示するための関数
def pipe_cou_display(total_area, method, NoLeak_PipeCount_dic, Leak_PipeCount_dic):
    pipe_inf = ["計算方法:" + str(method),
                "合計の受持ち面積(㎡):" + str(total_area),
                "侵入の恐れがない場合(本)",
                "A100:" + str(NoLeak_PipeCount_dic["A100"]),
                "A125:" + str(NoLeak_PipeCount_dic["A125"]),
                "A150:" + str(NoLeak_PipeCount_dic["A150"]),
                "A200:" + str(NoLeak_PipeCount_dic["A200"]),
                "侵入の恐れがある場合(本)",
                "A100:" + str(Leak_PipeCount_dic["A100"]),
                "A125:" + str(Leak_PipeCount_dic["A125"]),
                "A150:" + str(Leak_PipeCount_dic["A150"]),
                "A200:" + str(Leak_PipeCount_dic["A200"])]
    return pipe_inf
