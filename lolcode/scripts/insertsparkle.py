#!/usr/bin/python3
n = input("Message:\n")
o = ":sparkles: "+n+" :sparkles:"
import pyperclip
pyperclip.copy(o)
spam = pyperclip.paste()
