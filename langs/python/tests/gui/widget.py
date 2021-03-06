#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we show how to
use the Listbox widget.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from ttk import Frame, Label
from Tkinter import Tk, BOTH, Listbox, StringVar, END


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()


    def initUI(self):

        self.parent.title("Listbox")

        self.pack(fill=BOTH, expand=1)

        acts = ['Scarlett Johansson', 'Rachel Weiss',
            'Natalie Portman', 'Jessica Alba', 'Someone Else']

        with open('test.txt', 'rb') as f:

            lb = Listbox(self)
            for i in f:
                lb.insert(END, i)

        lb.bind("<<ListboxSelect>>", self.onSelect)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()


    def onSelect(self, val):

        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)


def main():

    root = Tk()
    ex = Example(root)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    root.geometry("500x450+500+500")
    #root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
