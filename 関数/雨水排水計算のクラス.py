class RdCount:
    def __init__(self, total_area, precipitation):
        self.total_area = total_area
        self.precipitation = precipitation
    
    #雨水排水設計基準
    def pipe_cou(self):
        #管径
        r_pipe = ["A100", "A125", "A150", "A200"]

        #簡略法(brief)
        #侵入の恐れなし
        brief_noleak_dic = {"A100": 120, "A125": 218, "A150": 353, "A200": 766}
        #侵入の恐れあり
        brief_leak_dic = {"A100": 60, "A125": 109, "A150": 176, "A200": 383}

        #補正法(correction)
        correction_noleak_dic = {}
        correction_leak_dic = {}
        for i in r_pipe:
            val1 = brief_noleak_dic[i] * (150 / self.precipitation)
            correction_noleak_dic[i] = val1
            val2 = brief_leak_dic[i] * (300 / self.precipitation)
            correction_leak_dic[i] = val2

        if self.precipitation < 150:
            noleak_dic = brief_noleak_dic
            leak_dic = brief_leak_dic
            self.method = "簡略法"
        else:
            noleak_dic = correction_noleak_dic
            leak_dic = correction_leak_dic
            self.method = "補正法"

        self.NoLeak_PipeCount_dic = {}
        self.Leak_PipeCount_dic = {}
        for j in r_pipe:
            NoLeak_ans = self.total_area / noleak_dic[j]
            NoLeak_pipe_cou = math.ceil(NoLeak_ans)
            self.NoLeak_PipeCount_dic[j] = NoLeak_pipe_cou

            Leak_ans = self.total_area / leak_dic[j]
            Leak_pipe_cou = math.ceil(Leak_ans)
            self.Leak_PipeCount_dic[j] = Leak_pipe_cou
        return self.method, self.NoLeak_PipeCount_dic, self.Leak_PipeCount_dic
    
    #Rhino上で情報を表示するための関数
    def pipe_cou_display(self):
        self.pipe_cou()
        pipe_inf = ["計算方法: " + str(self.method),
                    "合計の受持ち面積(㎡): " + str(self.total_area),
                    "侵入の恐れがない場合(本 + 1本)",
                    "A100: " + str(self.NoLeak_PipeCount_dic["A100"] + 1),
                    "A125: " + str(self.NoLeak_PipeCount_dic["A125"] + 1),
                    "A150: " + str(self.NoLeak_PipeCount_dic["A150"] + 1),
                    "A200: " + str(self.NoLeak_PipeCount_dic["A200"] + 1),
                    "侵入の恐れがある場合(本 + 1本)",
                    "A100: " + str(self.Leak_PipeCount_dic["A100"] + 1),
                    "A125: " + str(self.Leak_PipeCount_dic["A125"] + 1),
                    "A150: " + str(self.Leak_PipeCount_dic["A150"] + 1),
                    "A200: " + str(self.Leak_PipeCount_dic["A200"] + 1)]
        return pipe_inf

    
#-------------------------------------------------------------------------------------
pipe = RdCount(4000, 60)
b = pipe.pipe_cou_display()
print(b)
#-------------------------------------------------------------------------------------
#['計算方法: 簡略法', '合計の受持ち面積(㎡): 4000', '侵入の恐れがない場合(本 + 1本)', 'A100: 35', 'A125: 20', 'A150: 13', 'A200: 7', '侵入の恐れがある場合(本 + 1本)', 'A100: 68', 'A125: 38', 'A150: 24', 'A200: 12']

