# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-04-10 19:29:02
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-04-10 19:34:52


def reverse_score_list2(score_list: list) -> list[int]:
    return [int(str(score)[::-1]) for score in score_list]


score_list = [35, 46, 57, 91, 29]
print(reverse_score_list2(score_list))
