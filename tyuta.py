import sys
import os
import shutil


def init():
    path = r".\.wit"
    if not os.path.exists(path):
        os.makedirs(path)
    images_path = path + r"\images"
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    staging_area_path = path + r"\staging_area"
    if not os.path.exists(staging_area_path):
        os.makedirs(staging_area_path)



def add(folder_or_file_name):
    path = os.getcwd(
    wit_path = rf"{path}\.wit"
    if not os.path.exists(wit_path):
        raise OSError
    staging_area_path = rf"{wit_path}\staging_area"
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == folder_or_file_name:
                folder_path = os.path.join(root, dir)
                shutil.copytree(folder_path, f"{staging_area_path}/{folder_or_file_name}")
                return
        for file in files:
            if file == folder_or_file_name:
                file_path = os.path.join(root, file)
                shutil.copy(file_path, staging_area_path)
                return


main_arg = sys.argv[1]
match main_arg:
    case "init":
        init()
    case "add":
        add("temp1")