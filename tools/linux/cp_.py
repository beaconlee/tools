import shutil
import time
import os
import ini_


def add_timastamp():
  stamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
  return (stamp)


def rename_file(filename_without_timestamp):
  (file_without_suff, extention) = os.path.splitext(filename_without_timestamp)
  stamp = add_timastamp()
  file_add_timestamp = file_without_suff + stamp
  file_with_timestamp = file_add_timestamp + extention

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
  copy_files(ini_.local_path, ini_.dst_path, items)
