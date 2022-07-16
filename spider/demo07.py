import json
import urllib.request
import urllib.parse
import os

"""
ajax[GET]请求
爬取多页豆瓣电影排行
"""
base_path = '../resource/douban/'

base_url = 'https://movie.douban.com/j/chart/top_list?'

params = 'type=11&interval_id=100%3A90&action=&start=20&limit=20'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}


def create_request(page, limit=10):
    # 解码查询参数
    data = urllib.parse.unquote(params)
    # 解析查询参数为字典
    dict_params = dict(urllib.parse.parse_qsl(data))
    # print(type(dict_params), dict_params)
    # 对字典中的分页参数修改
    dict_params['start'] = (page - 1) * limit
    dict_params['limit'] = limit
    # print(type(dict_params), dict_params)

    # 将字典构造为查询参数，并编码
    new_params = urllib.parse.urlencode(dict_params)

    # 构造请求对象
    url = base_url + new_params
    print(url)

    return urllib.request.Request(url=url, headers=headers)


def get_content(request):
    # 发起请求，获取相应
    response = urllib.request.urlopen(request)
    # 解析相应，获取内容
    content = response.read().decode('utf-8')
    return content


def download_file(content, page):
    file_name = 'douban_movies' + '_{:0>3d}'.format(page) + '.json'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
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
