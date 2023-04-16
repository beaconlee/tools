import paramiko_
import ini_


if __name__ == '__main__':

  host = paramiko_.get_ssh()
  # 将远端remote_path目录中的所有文件get到本地local_path目录
  host.sftp_put_dir(ini_.upload_src_path, ini_.upload_dst_path)
  # # 将本地local_path目录中的所有文件put到远端remote_path目录
  # host.sftp_put_dir(remote_path, local_path)

# 运行结果
