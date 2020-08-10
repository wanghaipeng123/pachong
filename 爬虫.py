import urllib.request
import urllib.parse
import json
content=input('你好，请输入需要翻译的内容：')

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data={}
data['i']=content
data['from']='AUTO'
data['to']= 'AUTO'
data['smartresult']='dict'
data['client']= 'fanyideskweb'
data['salt']= '15969829625732'
data['sign']= 'c170772304d4b37c3544b12649ee488b'
data['lts']= '1596982962573'
data['bv']= '9915c65c9e78cfd742d6a24e66b85108'
data['doctype']= 'json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']= 'FY_BY_REALTlME'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
target = json.loads(html)
print('得到的翻译结果是：%s' %  (target['translateResult'][0][0]['tgt']))
