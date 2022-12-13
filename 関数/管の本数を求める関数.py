import math

#雨水排水設計基準
#precipitation:当該地域の換算最大降水量(mm/h)
def pipe_cou(total_area, precipitation):
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
        val1 = brief_noleak_dic[i] * (150 / precipitation)
        correction_noleak_dic[i] = val1
        val2 = brief_leak_dic[i] * (300 / precipitation)
        correction_leak_dic[i] = val2



    if precipitation < 150:
        noleak_dic = brief_noleak_dic
        leak_dic = brief_leak_dic
    else:
        noleak_dic = correction_noleak_dic
        leak_dic = correction_leak_dic

    NoLeak_PipeCount_dic = {}
    Leak_PipeCount_dic = {}
    for j in r_pipe:
        NoLeak_ans = total_area / noleak_dic[j]
        NoLeak_pipe_cou = math.ceil(NoLeak_ans)
        NoLeak_PipeCount_dic[j] = NoLeak_pipe_cou

        Leak_ans = total_area / leak_dic[j]
        Leak_pipe_cou = math.ceil(Leak_ans)
        Leak_PipeCount_dic[j] = Leak_pipe_cou
    return NoLeak_PipeCount_dic, Leak_PipeCount_dic
