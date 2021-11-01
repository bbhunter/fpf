import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help="Specify the file which contains URLs")
parser.add_argument('pattern', help="Specify the pattern - e.g.[xss, sqli, lfi, ssrf, ssti, redirect, rce, idor]")
parser.add_argument('-c', '--concurrency', help="Specify concurrency, default is 20", default=20, type=int)
args = parser.parse_args()
FILE = args.file
PATTERN = args.pattern
CONCURRENCY = args.concurrency