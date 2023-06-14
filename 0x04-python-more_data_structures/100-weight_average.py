#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res_score = 0
    res_weight = 0
    for i, j in my_list:
        res_score += i * j
        res_weight += j
    return res_score / res_weight if res_weight != 0 else 0
