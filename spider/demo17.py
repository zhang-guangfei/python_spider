import urllib.parse

url='__biz=Mzg5MjUxMzM5Mg==&mid=2247565452&idx=1&sn=c512ef97114f05150ac89218f25f6eb8&chksm=c03f7d93f748f485f8215207d034026e43c3adc32543663b26726ddda9e47cd4df85fedfbc8d#rd'

urllib.parse.quote(url,encoding='utf-8')
d=dict(urllib.parse.parse_qsl(url))
print(d)