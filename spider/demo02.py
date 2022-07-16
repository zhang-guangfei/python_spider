import urllib.request


# 下载
url_page='http://www.baidu.com'
urllib.request.urlretrieve(url_page, '../resource/baidu.html')

url_image = 'http://i0.hdslb.com/bfs/space/cfbacd89ebfd79968b0cf225d59fa74427859e60.png'
urllib.request.urlretrieve(url_image, '../resource/a.png')
