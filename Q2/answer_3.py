# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-04-10 19:35:21
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-04-10 21:58:14
from random import randint


def find_last_person2(n: int) -> int | None:
    if n == 0:
        return None
    people = list(range(1, n + 1))
    index = 0
    for _ in range(n - 1):
        index = (index + 2) % len(people)
        people.pop(index)
    return people[0]


n = randint(0, 100)
print(n,find_last_person2(n))
