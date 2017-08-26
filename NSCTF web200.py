# -*- coding:utf-8 -*-
import string
import base64
import codecs

key = 'a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws'
stf = ''

stf = base64.b64decode(codecs.encode(key,"rot_13")[::-1])
#之前为bytes格式
stf = str(stf,encoding = "utf-8")

flag = ""
for i in range(len(stf)):
	flag += chr(ord(stf[i])-1)

print(flag[::-1])