'''
Author: bquanli-linux bquanlinux@gmail.com
Date: 2023-04-15 14:28:36
LastEditors: bquanli-linux bquanlinux@gmail.com
LastEditTime: 2023-04-15 16:46:29
FilePath: /code/zipdemo/cp_.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import shutil
import time
import os
import ini_


def add_timastamp():
  ''' return timestamp mark'''
  stamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
  return (stamp)


def rename_file(filename_without_timestamp):
  '''add timestamp to filename'''
  (file_without_suff, extention) = os.path.splitext(filename_without_timestamp)
  stamp = add_timastamp()
  file_add_timestamp = file_without_suff + stamp
  file_with_timestamp = file_add_timestamp + extention
  # print filename_without_timestamp,file_with_timestamp
  os.rename(filename_without_timestamp, file_with_timestamp)


def copy_files(src_dir, dst_dir, items):
  results = []
  for item in items:
    src_path = os.path.join(src_dir, item)
    dst_path = os.path.join(dst_dir, item)
    if os.path.isfile(src_path):

      try:
        if (os.path.exists(os.path.dirname(dst_path)) != True):
          os.makedirs(os.path.dirname(dst_path))
          shutil.copy(src_path, dst_path)
          results.append((item, True, ''))
        else:
          shutil.copy(src_path, dst_path)
          results.append((item, True, ''))
      except Exception as e:
        results.append((item, False, str(e)))
    elif os.path.isdir(src_path):
      try:
        shutil.copytree(src_path, dst_path)
        results.append((item, True, ''))
      except Exception as e:
        results.append((item, False, str(e)))
    else:
      print(f'unknow : {src_path}')
      continue

  for item, success, reason in results:
    if success:
      rename_file(dst_path)
      print(f'{item} file was successfully copied and renamed!')
    else:
      print(f'{item} file copy failed, reason:{reason}')

def run_copy():
  items = [
      ini_.cp_filename
  ]
  copy_files(ini_.cp_src_path, ini_.cp_dst_path, items)
