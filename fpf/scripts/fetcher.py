import re
from fpf.scripts.colors import GRAY, GREEN, RESET, RED
from fpf.scripts.args import PATTERN, FILE

Found = []

def fetcher(each_pattern):
    with open(FILE) as File:
        read_f = File.readlines()
    for each_read in read_f:
        if re.findall(each_pattern, each_read):
            print(each_read, sep='', end='')
            Found.append(each_read)
