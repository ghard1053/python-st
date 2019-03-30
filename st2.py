
import random, datetime, json
from hoge import fuga

r = random.randint(1, 6)

datetime.date.today()
t = datetime.date.now()
t.strftime("%Y/%m/%d")


a_file = open("mt7_7.txt", encoding="utf-8")
s = a_file.read()
a_file.close()

a_file = open("test.txt", mode="w", encoding="utf-8")
a_file.write("hello\n")
a_file.write("world\n")
a_file.close()

a_file = open("test.txt", mode="w", encoding="utf-8")
try:
    a_file.write()
finally:
    a_file.close()


with open("test.txt", mode="w") as f:
    f.write("hello\n")
    f.write("world\n")

with open("mt7_7.txt", encoding="utf-8") as tf:
    for line in tf:
        print(line)

key = "find"
with open("mt7_7.txt", encoding="utf-8") as tf:
    for i, line in enumerate(tf):
        if line.find(key) >= 0:
            print(i+1, ":", line)


import json

data = {
  "no": 5,
  "code": ("jas", 1, 19),
  "src": "be quick to listen, slow to speak, slow to anger"
}

filename = "test.json"
with open(filename, "w") as fp:
    json.dump(data, fp)

with open(filename, "r") as fp:
    r = json.load(fp)
    print("no =", r["no"])
    print("code =", r["code"])
    print("src =", r["src"])


# コマンドラインツール
import sys

for i, v in enumerate(sys.argv):
    print(i, v)


import sys
import os

if len(sys.argv) <= 1:
    print("[USAGE] findtext (keyword)")
    sys.exit(0)

keyword = sys.argv[1]

for root, dirs, files in os.walk("."):
    for fi in files:
        result = []
        try:
            path = os.path.join(root, fi)
            with open(path, encodeing='utf-8') as f:
                for no, line in enumerate(f):
                    if line.find(keyword) >= 0:
                        line = line.strip()
                        s = "| {0:4}: {1}".format(no+1, line)
                        result.append(s)
        except:
            continue
        if len(result) > 0:
            print("+ file: " + fi)
            for li in result:
                print(li)

# ----------------
import sys
import os
import fnmatch
import datetime
import math

if len(sys.argv) <= 1:
    print("[USAGE] findfile [--name][--wild][--desc] name")
    sys.exit(0)

serch_mode = "name"
serch_func = lambda target, name : (target == name)
name = ""
desc_mode = False

for v in sys.argv:
    if v == "--name":
        serch_mode = "name"
        serch_func = lambda target, name : (target == name)
    elif v == "--wild":
        serch_mode = "wild"
        serch_func = lambda target, pat : fnmatch.fnmatch(target, pat)
    elif v == "--desc": desc_mode = True
    else:
        name = v

print("+ option")
print("| serch_mode=", serch_mode, name)
print("| desc_mode=", desc_mode)

for root, dirs, files in os.walk("."):
    for fname in files:
        path = os.path.join(root, fname)
        b = serch_func(fname, name)
        if b == False: continue
        if desc_mode:
            info = os.stat(path)
            kb = math.ceil(info.st_size / 1024)
            mt = datetime.datetime.fromtimestamp(info.st_mtime)
            s = "{0},{1}KB,{2}".format(path, kb, mt.strftime("%Y-%m-%d"))
            print(s)
        else:
            print(path)


import os

print("script path=", __file__)
print("script dir=", os.path.dirname(__file__))


# 正規表現

import re
pat = r"\d+"
str = "This pen is 100yen."
re.search(pat, str) # match='100'

import re

words = [
    "orange", "october", "octpus",
    "order", "banana", "baby", "busy"
]

pattern = r"oc.*"
print("oc- pattern = ", pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)

pattern = r"b.*y"
print("b- -y = ", pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)


# List Comprehensions

data = [ (i * 2 - 1) for i in range(1, 6) ]
data = [ i for i in range(1, 11) if i % 2 == 1 ]

base = [1, 2, 3]
result = [ (x, y) for x in base for y in base ]
result = [ (x, y) for x in base for y in base if x != y ]

res = [
    "Fizz Buzz" if i % 15 == 0 else "Fizz"
                if i %  3 == 0 else "Buzz"
                if i %  5 == 0 else str(i)
    for i in range(1, 21)
]
print("\n".join(res))

{ "h"+str(x) : x*5 for x in range(1, 4) }

( x**2 for x in [1, 2, 3] )


# decorator

def show_func_name(func):
    def wrapper(*args, **kwargs):
        print("--- start: " + func.__name__)
        res = func(*args, **kwargs)
        print("--- end: " + func.__name__)
        return res
    return wrapper

@show_func_name
def kakugen1():
    print("hello")
    print("world")

@show_func_name
def kakugen2():
    print("got it")

kakugen1()
kakugen2()

# --------

import time

def time_log(func):
    def wrapper(*args, **kwargs):
        import datetime
        start = datetime.datetime.today()
        print("--- start", func.__name__)

        result = func(*args, **kwargs)

        end = datetime.datetime.today()
        delta = end - start
        print("--- end", func.__name__, delta, "sec")
    return wrapper

@time_log
def test1():
    print("sleep 1sec")
    time.sleep(1)

@time_log
def test2():
    print("slee@ 2sec")
    time.sleep(2)

test1()
test2()
