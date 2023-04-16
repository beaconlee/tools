'''
Author: bquanli-linux bquanlinux@gmail.com
Date: 2023-04-15 13:51:18
LastEditors: bquanli-linux bquanlinux@gmail.com
LastEditTime: 2023-04-15 15:21:31
FilePath: /code/zipdemo/ini_.py
'''

from configparser import ConfigParser

config = ConfigParser()
# 传入读取文件的地址，encoding文件编码格式，中文必须
config.read('/code/zipdemo/config.ini', encoding='UTF-8')



unzip_path = config['unzip']['unzip_pwd']
unzip_filename = config['unzip']['unzip_filename']

cp_filename = config['cp']['cp_filename']
cp_src_path = config['cp']['cp_src_pwd']
cp_dst_path = config['cp']['cp_dst_pwd']


md5_path = config['md5']['md5_pwd']
md5_filename = config['md5']['md5_filename']
zip_filename = config['md5']['zip_filename']