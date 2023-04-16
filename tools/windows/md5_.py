import ini_
import hashlib


def get_md5sum():
  directory = ini_.put_src_pwd
  zipfilename = ini_.put_src_filename

  file_name = directory + "/" + zipfilename
  md5File = directory + '/' + 'md5.txt'

  fp = open(file_name, 'rb')
  content = fp.read()
  fp.close()
  m = hashlib.md5(content)
  file_md5 = m.hexdigest()

  fh = open(md5File, 'w', encoding='utf-8')
  fh.write(file_md5)
  fh.close()

