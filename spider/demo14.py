import time
import urllib.parse
import urllib.request
import json
import os
import urllib.error

"""
爬取p站图片


"""

url = 'https://api.pixivel.moe/v2/pixiv/illusts/sample?p=5'

img_base_url = 'https://proxy.pixivel.moe/img-master/img/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}

download_path = download_path = '../resource/pixiv/illusts/'


def get_request(page_number):
    split = url.split('?')
    base_url = split[0]
    params = split[1]

    params_dict = dict(urllib.parse.parse_qsl(params))

    params_dict['p'] = page_number

    params = urllib.parse.urlencode(params_dict)

    new_url = base_url + '?' + params

    request = urllib.request.Request(url=new_url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def parse_content(content, page):

    data = json.loads(content)['data']['illusts']

    list = json.dumps(data, indent=2, ensure_ascii=False)

    with open('{:0>3d}'.format(page) + '.json', 'w', encoding='utf-8') as file:
        file.write(list)
        file.flush()
    return data


# https://proxy.pixivel.moe/img-master/img/2017/07/25/09/44/47/64039863_p0_master1200.jpg
def create_url(info):
    # https://proxy.pixivel.moe/img-master/img
    img_base_url

    # 2011-02-23T20:54:38
    # 2017/07/25/09/44/47
    img_path = info['image'].replace('T', '/').replace('-', '/').replace(':', '/')

    # 64039863_p0_master1200.jpg
    img_file = '/' + str(info['id']) + '_p0_master1200.jpg'

    img_url = img_base_url + img_path + img_file
    return img_url


def download_data(img_url, title):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    file_name = title + '.jpg'

    full_name = download_path + file_name

    opener = urllib.request.build_opener()
    opener.addheaders = [('user-agent', headers['user-agent'])]
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(url=img_url, filename=full_name)
        print(img_url, title)
    except urllib.error.HTTPError as e:
        if e.code == '404':
            print(img_url, "没有找到资源...")
        else:
            print(img_url, 'HTTP Error %s: %s' % (e.code, e.msg))


if __name__ == '__main__':

    for page in range(1, 2):
        request = get_request(page)

        content = get_content(request)

        data = parse_content(content, page)

        for item in data:
            img_url = create_url(item)
            download_data(img_url, item['title'])
