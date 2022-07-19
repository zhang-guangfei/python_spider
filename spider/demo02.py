import urllib.request
"""
根据图片URL,下载图片到本地"""

# 下载
url_page='http://www.baidu.com'
urllib.request.urlretrieve(url_page, 'baidu.html')

url_image = 'http://i0.hdslb.com/bfs/space/cfbacd89ebfd79968b0cf225d59fa74427859e60.png'
urllib.request.urlretrieve(url_image, 'a.png')
