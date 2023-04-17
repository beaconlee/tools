python环境: Python 3.10.10

需要安装的python库:
  1. cryptography
  2. paramiko
  3. configparser


#### 第一次运行操作步骤
1. 配置tools下config.ini文件。

2. 配置tools/linux下config.ini文件。

3. 配置tools/linux/ini_.py加载config.ini路径
注意： 

1. linux端需要tools下linxu脚本文件，配置好linux文件夹下config.ini配置文件后, 可以使用start_upload.sh将linux文件上传到linux端。文件上传位置在tools/config.ini的[upload]字段中设置.

2. windows下配置好配置文件后，可直接运行脚本文件进行文件上传。


#### 非第一次运行操作步骤

运行tools下start_python.sh。


###### 可能出现的问题：
1. 出现乱码：windows终端与linxu终端字符集不同导致，更改windows和linux终端为同一字符集。
2. 加载配置文件出错：需要保持tools目录文件结构正确, 加载路径时相对路径。
3. ini_：KeyError: 'xxx'， config.ini文件里面配置的路径不对，或者ini_.py加载配置文件路径没有更改

