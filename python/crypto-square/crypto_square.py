# -*- coding:utf-8 -*-

from math import sqrt, ceil
import re

def prepare(text):
    r = re.compile("[a-z\d]")
    return r.findall(text.lower())

def encode(plain_text):
    pre_text = prepare(plain_text)
    row_length = ceil(sqrt(len(pre_text)))

    char_matrix = [[] for j in range(row_length)]
    for i, x in enumerate(pre_text):
        char_matrix[i % row_length].append(x)

    str_list = []
    for y in char_matrix:
        str_list.append("".join(y))

    return " ".join(str_list)
