import json
import urllib.request
import urllib.parse
import os
import time
"""
ajax[POST]请求
爬取bilibili up主视频bv号
"""
mid = '302417610'

bilibili_url = 'https://www.bilibili.com/video/'

base_path = '../resource/bilibili/'

base_url = 'https://api.bilibili.com/x/space/arc/search?'

params = 'mid=1285446&ps=30&tid=0&pn=2&keyword=&order=pubdate&jsonp=jsonp'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}


def create_request(page_number, page_size=10):
    dict_params = dict(urllib.parse.parse_qsl(params))
    '''
    {   
        'mid': '1285446',   #用户id
        'ps': '30',         #page_size
        'tid': '0',         #
        'pn': '2',          #page_number
        'order': 'pubdate', 
        'jsonp': 'jsonp'
    }
    '''
    dict_params['mid'] = mid if mid else '1285446'
    dict_params['pn'] = page_number
    dict_params['ps'] = page_size

    # 将字典构造为查询参数，并编码
    data = urllib.parse.urlencode(dict_params)

    # 构造请求对象
    url = base_url + data
    print(url)

    return urllib.request.Request(url=url, headers=headers)


def get_content(request):
    # 发起请求，获取相应
    response = urllib.request.urlopen(request)
    # 解析相应，获取内容
    content = response.read().decode('utf-8')

    return content


def get_data(content):
    data_dict = json.loads(content)
    data_list = data_dict.get('data').get('list').get('vlist')
    print(data_list[0])
    global up_name
    up_name = data_list[0].get('author')
    bv_list = [{'title': item['title'],\
                'BV_ID': item['bvid'],\
                'url': bilibili_url + item['bvid'],\
                'create_time':time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(item['created'])) \
                } \
               for item in data_list]

    return json.dumps(bv_list, indent=2, ensure_ascii=False)


def download_file(content, page):
    file_name = 'BVID' + '_{:0>3d}'.format(page) + '.json'
    full_path= base_path +up_name+'/'
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    with open(full_path + file_name, 'w', encoding='utf-8')as file:
        file.write(content)
        file.close()


if __name__ == '__main__':
    for page in range(1, 2):
        # 构造请求对象
        request = create_request(page, 50)
        # 获取响应内容
        content = get_content(request)
        data = get_data(content)
        download_file(data, page)
