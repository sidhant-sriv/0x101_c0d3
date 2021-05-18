#!/usr/bin/python3
x = str(input("\n"))
o = x.replace(" ",".   ")
import pyperclip
pyperclip.copy(o)
spam = pyperclip.paste()
