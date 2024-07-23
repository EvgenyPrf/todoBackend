import os


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def print_directory_contents(directory):
    for folder in os.listdir(directory):
        print(os.path.join(directory, folder))
