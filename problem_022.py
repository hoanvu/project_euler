# https://projecteuler.net/problem=22

import sys
sys.path.append('/home/hoanvu/anaconda2/envs/ds/lib/python2.7/site-packages/')
import string
import pandas as pd


data = pd.read_csv('./data/p022_names.txt')
d = list(data.columns.sort_values())


def get_sum(name):
    total = 0
    for ch in name:
        total += string.ascii_uppercase.index(ch) + 1
    return total * (d.index(name) + 1)


if __name__ == '__main__':
    total = 0
    for name in data:
        total += get_sum(name)

    print (total)