
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