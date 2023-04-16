'''
Author: bquanli-linux bquanlinux@gmail.com
Date: 2023-04-15 13:50:47
LastEditors: bquanli-linux bquanlinux@gmail.com
LastEditTime: 2023-04-15 15:08:24
FilePath: /code/zipdemo/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cp_
import unzip_
import md5_

if __name__ == '__main__':
  md5_.check_md5()

  unzip_.run_unzip()

  cp_.run_copy()
