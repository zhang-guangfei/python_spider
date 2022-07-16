import json
import urllib.request
import urllib.parse
import os
"""
ajax[POST]请求
爬取北京肯德基地址列表
"""
base_path = '../resource/kfc/'

base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}


def create_request(page, limit=10):
    # 请求体参数
    data = {
        'cname': '北京',
        'pageIndex': page,
        'pageSize': limit,
    }
    # 将字典构造为查询参数，并编码
    data = urllib.parse.urlencode(data).encode('utf-8')

    # 构造请求对象
    url = base_url
    print(url)

    return urllib.request.Request(url=url, data=data, headers=headers)


def get_content(request):
    # 发起请求，获取相应
    response = urllib.request.urlopen(request)
    # 解析相应，获取内容
    content = response.read().decode('utf-8')
    return content


def download_file(content, page):
    file_name = 'KFC_beijing_location' + '_{:0>3d}'.format(page) + '.json'
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    with open(base_path + file_name, 'w', encoding='utf-8')as file:
        file.write(json.dumps(json.loads(content), indent=2, ensure_ascii=False))
        file.close()


if __name__ == '__main__':
    for page in range(1, 10):
        # 构造请求对象
        request = create_request(page)
        # 获取响应内容
        content = get_content(request)
        download_file(content, page)
