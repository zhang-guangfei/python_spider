import json
import os
import urllib.parse
import urllib.request
import time

"""
爬取bilibili中，我的历史浏览记录
此url是通过本地调试发现的url
[GET]请求 
HTTPS 需要UA认证
cookie 需要登录
referer 防盗链

"""

mid = {
    'my': '212314714',
    '尚硅谷': '302417610',
    '银子': '1285446'
}

base_url = 'https://api.bilibili.com/x/web-interface/history/cursor?'

base_params = 'max=300742869&view_at=1657947375&business=archive'

download_path = '../resource/bilibili/history/'
headers = {
    "cookie": "buvid3=F6B0A4E7-18CA-1ABE-4A0C-A1D6B31480DF53977infoc; i-wanna-go-back=-1; buvid_fp=F6B0A4E7-18CA-1ABE-4A0C-A1D6B31480DF53977infoc; buvid_fp_plain=undefined; DedeUserID=212314714; DedeUserID__ckMd5=39d966a51528b3b3; rpdid=|(J~RY|J~ulR0J'uYlkkRmR~); b_ut=5; nostalgia_conf=-1; LIVE_BUVID=AUTO1316525054514659; CURRENT_BLACKGAP=0; blackside_state=0; is-2022-channel=1; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; SESSDATA=c3119c6a%2C1673511980%2C217c1%2A71; bili_jct=e6ea2334a3e7180151ced12c7b366fff; sid=8rrougp0; bp_video_offset_212314714=683423133480255500; fingerprint=8262d04bf3739a45f34a1c3c0cbe7245; innersign=1",
    "referer": "https://www.bilibili.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
}


def create_request():
    # 1.解析原url参数
    params_dict = dict(urllib.parse.parse_qsl(base_params))
    # 2.编辑参数
    params_dict['max'] = 813394634
    params_dict['view_at'] = int(time.time())
    params_dict['business'] = 'archive'
    print(json.dumps(params_dict, indent=2, ensure_ascii=False))

    # 3.构造新url参数，不需要utf-8编码
    new_params = urllib.parse.urlencode(params_dict)

    # 4.构造新url
    full_url = base_url + new_params
    print(full_url)
    # 5.构造请求对象 url，method,headers
    request = urllib.request.Request(url=full_url, headers=headers, method='GET')
    return request


def get_content(request):
    # 发起请求，获取响应对象
    response = urllib.request.urlopen(request)
    # 解码响应内容
    content = response.read().decode('utf-8')
    print('content:', type(content), content)
    return content


def parse_content(content):
    # 去掉前后缀，保留json字符串
    # content = content.split('(', 1)[1].rsplit(')', 1)[0]
    # 解析为字典格式
    data = json.loads(content)

    data = [{ \
        'title': item['title'], \
        'bvid': item['history']['bvid'], \
        'author_name': item['author_name'], \
        'author_mid': str(item['author_mid']), \
        'view_at': time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(item['view_at'])) \
        } \
        for item in data['data']['list']]

    return json.dumps(data, indent=2, ensure_ascii=False)


def dict_slice(data: dict, keys: list):
    new_dict = {}
    for key in keys:
        new_dict[key] = data.get(key)
    return new_dict


def download_data(data, page=1):
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    file_name = '{:0>3d}'.format(page) + '.json'
    full_name = download_path + file_name
    print('output:',full_name)
    with open(full_name, 'w', encoding='utf-8') as file:
        file.write(data)
        file.flush()


if __name__ == '__main__':
    # 构造请求对象
    request = create_request()
    # 发起请求，获得响应
    content = get_content(request)
    # 解析响应内容
    data = parse_content(content)
    # 保存为json文件
    download_data(data)
