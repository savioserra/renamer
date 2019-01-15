import re
import os
from source.lib.exceptions.invalid_filename_exception import InvalidFilenameException


def get_file_extension(filename):
    return '.' + re.sub(r'.*\.', '', filename)


def find_match(filename, targets):
    # Format: XXXXX_XX.jpg
    if not re.fullmatch(r'\d+_\d+.[\w\d_]+', filename):
        raise InvalidFilenameException(f'Incorrect file name: {filename}. Expected: XXXXX_XX.')

    pattern = re.sub(r'\..*$', '', filename, count=1)

    args = pattern.split('_')
    ref, number = args[0], int(args[1])

    for target in targets:
        if ref in target:
            if number == 1:
                return target
            return target + f'_{number - 1}'
    return None


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
