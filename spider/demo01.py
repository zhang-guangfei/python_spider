import urllib.request

url = 'http://www.baidu.com'
# 发送请求
response = urllib.request.urlopen(url)
print(type(response))

# HTTPResponse
# read readline readlines getcode geturl getheaders

# 解码
content = response.read().decode('utf-8')

print(content)

