"""Helper utils for pytest
"""


def read_file_to_string(file_name):
    """Read file from disk and return string with file contents.
    """
    with open(file_name, 'r') as stream:
        output = stream.read()
    return output


def read_file_to_list(file_name):
    """Read file from disk and return list with file contents.
    """
    with open(file_name, 'r') as stream:
        output = stream.readlines()
    return output
