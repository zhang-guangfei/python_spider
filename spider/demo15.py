import requests
from lxml import etree
import os
import time
"""

爬取公众号【图无尽】的每日推荐壁纸
"""
download_path = '../resource/图无尽/'

url = "http://mp.weixin.qq.com/s?__biz=Mzg5MjUxMzM5Mg==&mid=2247565452&idx=1&sn=c512ef97114f05150ac89218f25f6eb8&chksm=c03f7d93f748f485f8215207d034026e43c3adc32543663b26726ddda9e47cd4df85fedfbc8d#rd"

today_time=time.strftime('%Y%m%d')

def get_urls():
    response = requests.get(url=url)
    text = response.text
    html = etree.HTML(text)
    urls = html.xpath('//*[@id="js_content"]//img[@class="rich_pages wxw-img"]/@data-src')
    urls = [str(url) for url in urls]
    return urls


def download_file(url, index):
    try:
        response = requests.get(url=url)
        file_name = download_path  +'/{:0>2d}'.format(index) + '.jpg'
        with open(file_name, 'wb') as file:
            file.write(response.content)
            file.close()
        print(url)
    except Exception as e:
        print('出错了：', e, url)


if __name__ == '__main__':
    urls = get_urls()
    download_path+=today_time
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    for index, url in enumerate(urls):
        download_file(url, index)
