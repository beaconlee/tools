import md5_
import paramiko_
import zip_

if __name__ == "__main__":
  zip_.get_zip()
  md5_.get_md5sum()
  paramiko_.upload_zip()