import urllib.request
import urllib.parse
import time
import hashlib

import json

# This program is a web crawler of translation website fanyi.youdao.com
# The website itself uses some anti-web crawler algorithms to prevent people
# to get its translation content easily, but after looking through its source code, I
# managed to crawl the contents

# The request url
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'  # 上一次群里面那个失效了 把_o去掉就可以了 7
# 找出每次提交都变化的值
u = 'fanyideskweb'
print('============================Youdao Web Crawler=========================')
d = input('Please enter words to translate：')

# The source code for 'salt' variable is based on time：
# f = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))

f = str(int(time.time() * 1000))
c = "rY0D^0'nM0}g5Mm1z%1G4"
g = hashlib.md5()
g.update((u + d + f + c).encode('utf-8'))

# header
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'
head['Host'] = 'fanyi.youdao.com'
head['Referer'] = 'http://fanyi.youdao.com/'

# data
data = {}
data['i'] = d  # 这是我们要翻译的字符串
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = u
data['salt'] = f  # 当前时间戳。
data['sign'] = g.hexdigest()  # 签名字符串。
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CL1CKBUTTON'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

# request
req = urllib.request.Request(url, data, head)

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
print('Translation result： %s ' % (target['translateResult'][0][0]['tgt']))
