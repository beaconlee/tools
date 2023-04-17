from configparser import ConfigParser

config = ConfigParser()
# 传入读取文件的地址，encoding文件编码格式，中文必须
config.read('/tools/linux/config.ini', encoding='UTF-8')


local_path = config['pwd']['local_path']
dst_path = config['pwd']['dst_path']


unzip_filename = config['unzip']['unzip_filename']

cp_filename = config['cp']['cp_filename']

md5_filename = config['md5']['md5_filename']
zip_filename = config['md5']['zip_filename']
