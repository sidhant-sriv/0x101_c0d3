word = str(input())

words = [ord(i) for i in word]
words = [i - 96 for i in words]
print(sum(words))
