
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