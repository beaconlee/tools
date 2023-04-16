import ini_
import pathlib
import zipfile

def get_zip():
   
  # directory = ini_.file_pwd + '/'
  zipDirectory = ini_.put_src_pwd + '/' + ini_.put_src_filename
  directory = pathlib.Path(ini_.file_pwd)
  with zipfile.ZipFile(zipDirectory, mode="w") as archive:
    for file_path in directory.iterdir():
        archive.write(file_path, arcname=file_path.name)


  # directory = pathlib.Path(directory)
  # with zipfile.ZipFile(zipDirectory, mode="w") as archive:
  #   for file_path in directory.iterdir():
  #       archive.write(file_path, arcname=file_path.name)

# def get_zip():

#   directory = ini_.file_pwd
#   files = os.listdir(directory)
#   zipfilename = ini_.put_src_filename
#   zipDirectory = ini_.put_src_pwd

#   with zipfile.ZipFile(zipDirectory, 'w') as zip:
#     for file in files:
#       file_path = os.path.join(directory, file)
#       zip.write(file_path)


# get_zip()
# directory = 'zip'
# files = os.listdir(directory)

# with zipfile.ZipFile('zipfile.zip', 'w') as zip:
#     for file in files:
#         file_path = os.path.join(directory, file)
#         zip.write(file_path)

# How to Zip All Files in a Directory


# directory = 'zip/'
# files = pathlib.Path(directory)

# with zipfile.ZipFile('zipfile.zip', 'w') as archive:
#     for file in files.iterdir():

#         archive.write(file, arcname=file.name)



