import os
import shutil


class FileHandler:
    base_path = None
    working_directory = os.getcwd()

    @staticmethod
    def create_dir(path):
        os.makedirs(path)

    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        for root, dirs ,files in os.walk(cls.working_directory,topdown=False):
            for dir in dirs:
                if dir==".wit":
                    cls.base_path = os.path.join(root,dir)
                    return cls.base_path


        # raise Exception("Not a wit repository")

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            pass
            # TODO: handle file doesn't exist

    @classmethod
    def copy_item(cls, origin, target):
        pass
