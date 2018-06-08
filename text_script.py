#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import os
import io

import sys

reload(sys)
sys.setdefaultencoding('utf8')

lists = [
    {'key': 'TOKEN', 'exp': r'token="(\w*?)"'},
    {'key': 'PUBLIC_KEY', 'exp': r'n.setPublicKey\("`(.*?)`"\)'},
    {'key': 'PRIVATE_KEY', 'exp': r'n.setPrivateKey\("`(.*?)`"\)'},
    {'key': 'BASE_URL', 'exp': r'baseURL="(.*?)"'},
    {'key': 'APP_VERSION', 'exp': r'\$\.get\("(.*?)",'},
    {'key': 'IOS_DOWNLOAD_URL', 'exp': r'https://www.pgyer\.com/o5Ee'},
    {'key': 'VIDEO_RECOMMEND', 'exp': r'var url_video_recommend = "(.*?)";'},
    {'key': 'VIDEO_INFO', 'exp': r'var url_video_info = "(.*?)";'},
    {'key': 'SHOP_H5', 'exp': r"var url_shop_h5 = '(.*?)';"},
]


def vue_js_path(root_path='./dist/static/js'):
    abspath = os.path.abspath(root_path)
    files = os.listdir(abspath)
    for file in files:
        if re.match(r'^app.+\.js$', file):
            abspath = os.path.join(root_path, file)
            return abspath
    return None


def replace(text):
    search(text)
    for item in lists:
        if item.get('value', None) and item.get('env', None):
            text = text.replace(item.get('value'), item.get('env'))
    return text


def search(text):
    for item in lists:
        if item.get('env', None):
            result = re.findall(item.get('exp'), text)
            if len(result) != 0:
                item['value'] = result[0]
    print(lists)


def get_environ_value():
    for item in lists:
        value = os.environ.get(item['key'])
        item['env'] = value


def open_file(path):
    file = io.open(path, 'r', encoding='utf-8')
    if file is None:
        raise ValueError('File does not exist')
    text = file.read()
    text = replace(text)
    file.close()
    save_file(path, text)


def save_file(path, text):
    # os.remove(path)
    file = io.open(path, 'wb')
    text = text.encode('utf-8')
    text = unicode(text, 'utf-8')
    import codecs
    file.write(codecs.BOM_UTF8)
    file.write(text)
    file.close()


def main():
    get_environ_value()
    args = sys.argv[1:]
    for path in args:
        abspath = os.path.abspath('./' + path)
        open_file(abspath)

    if len(args) == 0:
        path = vue_js_path()
        open_file(path)


if __name__ == '__main__':
    main()
