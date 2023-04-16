from configparser import ConfigParser

config = ConfigParser()
# 传入读取文件的地址，encoding文件编码格式，中文必须
config.read('config.ini', encoding='UTF-8')

host = config['baseconf']['host']
port = config['baseconf']['prot']
username = config['baseconf']['user']
password = config['baseconf']['password']

file_pwd = config['zip']['pwd']

put_src_pwd = config['put_source']['pwd']
put_src_filename = config['put_source']['filename']

put_dst_pwd = config['put_destination']['pwd']
put_dst_filename = config['put_destination']['filename']

upload_src_path = config['upload']['upload_src_path']
upload_dst_path = config['upload']['upload_dst_path']