import re
import sys
import pyperclip
pattern = re.compile(sys.argv[2])

wordlistpath = "/home/sidhant/Documents/tea_mudae.txt"
res = []
for i in open(wordlistpath):
    for match in re.finditer(pattern,i):
        res.append(i[:-1])
res = sorted(res,key=len)
puts = ' '.join(res[:int(sys.argv[1])])
print(puts)
pyperclip.copy(puts)
spam = pyperclip.paste()
#print(res)
