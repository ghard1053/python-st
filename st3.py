
# --------
import tkinter.messagebox as mb

ans = mb.askyesno("question", "Do you like coffee??")
if ans == True:
    mb.showinfo("yes", "me too")
else:
    mb.showinfo("no", "really?")

# --------
import tkinter.filedialog as fd

path = fd.askopenfilename(
    title = "対象ファイルを選択",
    filetypes = [('HTML', '.html')]
)
print(path)

# --------
from tkinter import *
import tkinter.messagebox as mb

def say_hello():
    mb.showinfo("greeting", "hello")

root = Tk()
root.title('greeting')

desc_label = Label(text = "push button")
desc_label.pack()

hello_button = Button(
    text = "greeting",
    width = 10, height = 3,
    command = say_hello
)
hello_button.pack()

root.mainloop()

# --------
from tkinter import *

def count_text(event):
    s = main_text.get(1.0, END)
    info_label.config(text = "{0}".format(len(s)))

root = Tk()
root.title('テキストカウンタ')

main_text = Text(root)
main_text.bind("<Key>", count_text)
main_text.pack()

info_label = Label(root)
info_label.pack()

root.mainloop()


# --------
import cgi

form = cgi.FieldStorage()
mode = form.getvalue("mode", default = "")
print("mode = ", mode)
for k in form.keys():
    print(k, "=", form.getvalue(k))

# --------
import cgi

form = cgi.FieldStorage()

if (not 'vi' in form) or (not 'v2' in form):
    print("""

    """)
else:
    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")
    try:
        ans = int(v1) + int(v2)
    except:
        ans = 0
    print(ans)

# --------

import cgi
import cgitb
import os.path
import html

cbitb.enable()

FILE_LOG = "chat-log.txt"

def print_html(body):
    # 
    # print(**.format(body))

def mode_read(form):
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            log = f.read()
    print_html(log)

def jump(url):
    # 

def mode_write(form):
    name = form.getvalue("name", "no name")
    body = form.getvalue("body", "")
    name = html.escape(name)
    body = html.escape(body)
    with open(FILE_LOG, "a+", encoding='utf-8') as f:
        f.write("<p>{0}: {1}</p><hr>\n".format(name, body))
    jump('chat.py')

def main():
    form = cgi.FieldStorage()
    mode = form.getvalue("mode", "read")
    if mode == "read": mode_read(form)
    elif mode == "write": mode_write(form)
    else: mode_read(form)

if __name__ == "__main__":
    main()


# --------

import os, sys, math
from sklearn import datasets, svm
from sklearn.externals import joblib

DIGITS_PKL = "digit-clf.pkl"

def train_digits():
    digits = datasets.load_digits()
    data_train = digits.data
    label_train = digits.target
    clf = svm.SVC(gamma = 0.01)
    clf.fit(data_train, label_train)

    joblib.dump(clf, DIGITS_PKL)
    print("", DIGITS_PKL)
    return clf

def predict_digits(data):
    if not os.path.exists(DIGITS_PKL):
        clf = train_digits()
    clf = joblib.load(DIGITS_PKL)
    n = clf.predict([data])
    print("", n)

def image_to_data(imagefile):
    import numpy as np
    from PIL import Image
    image = Image.open(imagefile).convert('L')
    image = image.resize((8, 8), Image.ANTIALIAS)
    img = np.asarray(image, dtype = float)
    img = np.floor(16 - 16 * (img / 256))
    # import matplotlib.pyplot as plt
    # plt.imshow(img)
    # plt.gray()
    # plt.show()
    img = img.flatten()
    print(img)
    return img

def main():
    if len(sys.argv) <= 1:
        print("")
        return
    imagefile = sys.argv[1]
    data = image_to_data(imagefile)
    predict_digits(data)

if __name__ == '__main__':
    main()

