'''
Author: bquanli-linux bquanlinux@gmail.com
Date: 2023-04-15 13:50:27
LastEditors: bquanli-linux bquanlinux@gmail.com
LastEditTime: 2023-04-15 16:47:14
FilePath: /code/zipdemo/md5_.py
'''
import ini_
import hashlib


def get_zipfile_md5sum():
  directory = ini_.md5_path
  zipfilename = ini_.zip_filename

  file_name = directory + "/" + zipfilename

  fp = open(file_name, 'rb')
  content = fp.read()
  fp.close()
  m = hashlib.md5(content)
  file_md5 = m.hexdigest()

  return file_md5

def check_md5():
  directory = ini_.md5_path
  md5filename = ini_.md5_filename

  open_file = directory + '/' + md5filename

  file_object = open(open_file)

  try:
      file_context = file_object.read() #file_context是一个string，读取完后，就失去了对test.txt的文件引用
      if file_context == get_zipfile_md5sum():
        print("md5 verification is successful!")
      #  file_context = open(file).read().splitlines()
      # file_context是一个list，每行文本内容是list中的一个元素
  finally:
      file_object.close()