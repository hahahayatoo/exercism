# -*- coding: utf-8 -*-
import math

def prime_factors(given_number):
    table = sieve(given_number)
    return prime_search(given_number, table)

def sieve(given_number):
    limit = int(math.sqrt(given_number))
    ans = [2, 3]
    if limit < 5:
        return ans
    search_list = [x for x in range(5, limit + 1) if x % 2 != 0]

    while(math.sqrt(limit) > search_list[0]):
        ans.append(search_list[0])
        search_list = [x for x in search_list if x % search_list[0] != 0]
    ans += search_list
    return ans

def prime_search(num, table):
    ans = []
    while len(table) != 0 and num != 1:
        if num % table[0] == 0:
            num /= table[0]
            ans.append(table[0])
        else:
            table.pop(0)
    if num != 1:
        ans.append(num)
    return ans
