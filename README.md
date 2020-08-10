# 通过Python访问有道进行翻译
## 一、编程步骤
1. 打开**有道网页**
2. 点击检查元素
3. 点击*Network*
4. 点击Headers,找到Request URL
5. 找到From Data
6. 打开Python写程序

```Python
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
```

## 二、运行结果
### 可以对文本进行英汉互译

例如
```python
你好，请输入需要翻译的内容：软件工程
得到的翻译结果是：Software engineering
```
```python
你好，请输入需要翻译的内容：hope
得到的翻译结果是：希望
```