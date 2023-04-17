import ini_
import pathlib
import zipfile

def get_zip():
  zipDirectory = ini_.put_src_pwd + '/' + ini_.put_src_filename
  directory = pathlib.Path(ini_.file_pwd)
  with zipfile.ZipFile(zipDirectory, mode="w") as archive:
    for file_path in directory.iterdir():
        archive.write(file_path, arcname=file_path.name)

