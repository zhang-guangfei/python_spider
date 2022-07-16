import urllib.request
import urllib.parse
import json

# Post请求
# 百度翻译

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': 'spider'
}
data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'}

request = urllib.request.Request(
    url=url,
    data=data,
    headers=headers
)
print(request)
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
content = json.loads(content)

print(content)

