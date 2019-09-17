#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from Tkinter import *

    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=500, bg='green')
    for i in range(20):
        canvas.create_oval(200 - top, 250 - bottom, 200 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()