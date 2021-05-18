x = str(input("\n"))
s = int(input("Number of spaces\n")) or 1
res = ""
for i in x:
    res += i + s*" "
import pyperclip
pyperclip.copy(res)
spam = pyperclip.paste()
