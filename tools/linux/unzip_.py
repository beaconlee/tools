'''
Author: bquanli-linux bquanlinux@gmail.com
Date: 2023-04-15 13:50:38
LastEditors: bquanli-linux bquanlinux@gmail.com
LastEditTime: 2023-04-15 16:45:57
FilePath: /code/zipdemo/unzip_.py

'''
import ini_
import zipfile

def run_unzip():

  directory = ini_.unzip_path
  filename = ini_.unzip_filename

  unzip = directory + '/' + filename

  try:
      with zipfile.ZipFile(unzip, mode="r") as archive:
        archive.extractall(directory)
        print("unzip the file successfully.!")
  except Exception as e:
        print(e)

