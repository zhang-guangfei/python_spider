import urllib.request
import urllib.parse

# url参数unicode编码

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'}

url = 'https://www.baidu.com/s?wd='

#汉字转unicode编码
name = '周杰伦'
name = urllib.parse.quote(name)

request = urllib.request.Request(url=url+name, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
