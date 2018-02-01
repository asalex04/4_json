import json
from sys import argv
import os


def load_data(filepath):
    if os.path.isfile(filepath) and filepath.endswith(".json"):
       with open(filepath, 'r', encoding='utf-8') as my_file:
           return json.loads(my_file.read())
    else:
        print('File not found or not json format')


def pretty_print_json(json_content):
    print(json.dumps(
        json_content,
        indent=4,
        sort_keys=True,
        ensure_ascii=False,
    ))


if __name__ == '__main__':

    pretty_print_json(load_data(argv[1]))
