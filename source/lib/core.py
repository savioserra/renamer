import re
from source.lib.exceptions.InvalidFilenameException import InvalidFilenameException


def get_file_extension(filename):
    return '.' + re.sub(r'.*\.', '', filename)


def find_match(filename, targets):
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
