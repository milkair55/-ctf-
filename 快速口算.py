# coding=utf-8
import requests
import re

url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
req = requests.session()
get = req.get(url)
r = re.findall(r'<br/>[\d|\D](.*?)=<', get.text)[0].strip()
print(eval(r))
post = req.post(url, data={'v': eval(r)})
key = re.findall(r'<body>(.*?)</', post.text)[0].strip()
print(key)