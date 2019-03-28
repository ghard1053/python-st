
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