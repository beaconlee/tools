import ini_
import hashlib


def get_zipfile_md5sum():
  directory = ini_.local_path
  zipfilename = ini_.zip_filename

  file_name = directory + "/" + zipfilename

  fp = open(file_name, 'rb')
  content = fp.read()
  fp.close()
  m = hashlib.md5(content)
  file_md5 = m.hexdigest()

  return file_md5

def check_md5():
  directory = ini_.local_path
  md5filename = ini_.md5_filename

  open_file = directory + '/' + md5filename

  file_object = open(open_file)

  try:
      file_context = file_object.read() 
      if file_context == get_zipfile_md5sum():
        print("md5 verification is successful!")

  finally:
      file_object.close()