# -*- coding: utf-8 -*-
import math
import re

class Caesar(object):
    def __init__(self):
        self.salt = "d"

    def prepare(self, text):
        r = re.compile("[a-z]")
        return r.findall(text.lower())

    def key_gen(self, plain):
        salt = self.salt
        plain_len = len(plain)
        salt_len  = len(salt)

        return salt * math.ceil(plain_len / salt_len)

    def slide(self, source, key, sign):
        result=""
        for s, k in zip(source, key):
            r = ord(s) + (ord(k) - ord("a")) * sign
            result += chr(ord("a") + (r - 19) % 26)
        return result

    def encode(self, plain):
        plain = self.prepare(plain)
        key = self.key_gen(plain)
        return self.slide(plain, key, 1)

    def decode(self, cryptogram):
        cryptogram = self.prepare(cryptogram)
        key = self.key_gen(cryptogram)
        return self.slide(cryptogram, key, -1)

class Cipher(Caesar):
    def __init__(self, salt="d"):
        self.salt = salt
