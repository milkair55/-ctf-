import itertools as its
words = "1234567890"
r = its.product(words,repeat = 4)
dic = open("pass1.txt","a")
for i in r:
	dic.write("".join(i))
	dic.write("".join("\n"))
dic.close()