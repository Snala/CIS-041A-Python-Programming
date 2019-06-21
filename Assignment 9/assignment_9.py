from tkinter import filedialog
from tkinter import *
from collections import OrderedDict
import operator

root = Tk()


def get_count():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text", ".txt"), ("Log", ".log"), ("all files", "*")))

    # I know how to create an ascii list, but not a dictionary, so lets to it with comprehension.
    ascii_list = list(map(chr, range(97, 123)))
    ascii_dict = {i: 0 for i in ascii_list}

    with open(root.filename) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            try:
                if c.lower() in ascii_list:
                    ascii_dict[c] = ascii_dict.get(c) + 1
            except TypeError:
                pass

    sorted_ascii_dict = OrderedDict(sorted(ascii_dict.items(), key=operator.itemgetter(1)))

    return sorted_ascii_dict

class tk_draw:
    def __init__(self):
        self.master = Tk()
        self.master.geometry("1024x768")
        frame1 = Frame(self.master)
        self.master(mainloop())


count = get_count()
data = list(count.values())
tk_draw()
