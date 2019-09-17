#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 20):
        canvas.create_oval(400 - k, 300 - k, 400 + k, 300 + k, width=2)
        k += j
        j += 1.5

    mainloop()