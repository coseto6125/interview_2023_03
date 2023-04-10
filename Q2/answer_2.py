# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-04-10 19:35:21
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-04-10 20:14:44

from collections import Counter

celebrate_text = "Hello welcome to Cathay 60th year anniversary"

def calc_word_count(c_string: str) -> None:
    result = Counter(c.upper() for c in c_string if c.isalnum())
    print('\n'.join(f"{k} {v}" for k, v in sorted(result.items())))

calc_word_count(celebrate_text)