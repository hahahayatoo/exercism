# -*- coding: utf-8 -*-

def encode(original_data):
    compressed_data = ''
    num = 0
    target = original_data[0]

    for x in original_data:
        if target == x:
            num += 1
        else:
            compressed_data += encode_join(target, num)
            target = x
            num = 1
    else:
        compressed_data += encode_join(target, num)
    return compressed_data

def decode(compressed_data):
    original_data = ''
    num = ''
    for x in compressed_data:
        if x.isdigit():
            num += x
        else:
            if not num:
                original_data += x
            else:
                original_data += (x * int(num))
            num = ''
    return original_data

def encode_join(target, num):
    if num == 1:
        num = ''
    return (str(num) + target)
