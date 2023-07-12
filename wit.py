from FileHendler import FileHandler
import os
import  logging


class WitException(Exception):
    pass


class Wit:



    logging.basicConfig(level=logging.DEBUG)
    base_logger = logging.getLogger("wit_logger")

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():

            Wit.base_logger.info("check if wit is exist")
            raise WitException("Already exists")

        else:
            FileHandler.create_dir(".wit")
            FileHandler.create_dir(".wit/images")
            FileHandler.create_dir(".wit/staging_area")

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        full_path = FileHandler.validate_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit():
        pass
Wit.init()