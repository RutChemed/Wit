
import sys
import os




class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            # handle nested wits
            pass
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


class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        pass


if __name__ == "__main__":
    # TODO: handle edge cases
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)
    print("rut")

