import requests
import os
import json
import time

"""
爬取公众号【图无尽的所有文章】

"""

url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
    'cookie': 'appmsglist_action_3884832970=card; RK=i3e9j7OFaF; ptcz=e7cdccb474be8b1331f9757fe1463e07a526d5b3d3992c30b64597d0ca41d31f; pac_uid=0_b591ae89277b6; iip=0; pgv_pvid=3229045550; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; ua_id=4on5MpXEIFjKmFhQAAAAAMjf-8V0jZpsHz3EHDrgSaA=; wxuin=58212493517053; uuid=0756175ac7da2193307aa3f840e33084; cert=2R71WG42dPdMZhUsmWJhdPqPm_MovUq9; sig=h01e653a5bf208e84ac79ac5b0d8bfa1bb0dad41d82d77f95aeb4bea47a41d90e7916764c0fbbab746a; uin=o1204772017; skey=@8y3ZHHhB2; data_bizuin=3884832970; data_ticket=81k3GGNCafyOF97P7AvqzR9UscD/DU/WCnunT7BZZV/FOeze8+atOqEbyuZtQgTf; master_key=Ue3W/7vn7+6PGUSoziDCefwdxSH0IRe+wwYFfgsNs5A=; master_user=gh_4877ada0ec38; master_sid=MEk3dGZVYnkxcnpJVHZXbjVzQVd5Z1FaMXBCUEZlcGtOc1oxOGFZVGl1b2RKVkI5OXlEN0d3SkQ1THNfUUV1STBMTzY1RzBxc2pWUjRad28zemZXc3R3MjVIckg5Q21WOFdNSWRoQWJFUmZaTFRsRldqdmJ0TG41VFc3M1dkNXl4RlZLWlprMFlMTGFjeDJm; master_ticket=ce20137cb5be9d27230a3fdd1d89dd61; bizuin=3884832970; pgv_info=ssid=s1456173600; media_ticket=fdf550996911eb02187031355db7243a4b1b7ded; media_ticket_id=3884832970; slave_user=gh_4877ada0ec38; slave_sid=ZVdEdnNhZHJvend5Y1JDaDYxc0ZnMURGR2JIUUp5Z3lRSmtRRkx6azNTTGxuemtYUmZZc3FDb0tLeXZRYzFkX2ljQ3RwanJLcVFBZW5KWDlOM3NZNjVLc19HNHd1TThHQkJacnhPUHRIdEkyM2ZWOGdTeDRMRkdLQXAzTUpuT1o5Y1pwenEwS2RXSUtBQWEw',
    'referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=77&createType=0&token=1087916783&lang=zh_CN'
}

download_path = '../resource/图无尽/json/'

params = {
    'action': 'list_ex',
    'begin': 0,
    'count': 10,
    'fakeid': 'Mzg5MjUxMzM5Mg==',
    'type': 9,
    # 'query':,
    'token': 1087916783,
    'lang': 'zh_CN',
    'f': 'json',
    'ajax': 1,
}


def get_content():
    response = requests.get(url=url, params=params, headers=headers)
    text = response.text
    info = json.loads(text)
    info = info['app_msg_list']
    info = [{ \
        'title': item['title'], \
        'aid': item['aid'], \
        'link': item['link'], \
        'create_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['create_time'])), \
        'appmsgid': item['appmsgid'], \
        } \
        for item in info]
    text = json.dumps(info, indent=2, ensure_ascii=False)
    return text


def download_file(content):
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    try:
        file_name = download_path + 'info.json'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
            file.close()
    except Exception as e:
        print('出错了：', e)


if __name__ == '__main__':
    content = get_content()
    download_file(content)
