import os
import json


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def print_directory_contents(directory):
    for folder in os.listdir(directory):
        print(os.path.join(directory, folder))


def json_dumps(value):
    return json.dumps(value, indent=4)


def json_loads(value):
    return json.loads(value)


def write_json_to_file(filename: str, content: dict):
    with open(filename, 'w') as f:
        json.dump(content, f)


def read_json_from_file(filename: str):
    with open(filename, 'r') as f:
        return json.load(f)
