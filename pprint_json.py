import json
from sys import argv
import os


def load_data(filepath):
   with open(filepath, 'r', encoding='utf-8') as my_file:
       return json.loads(my_file.read())


def pretty_print_json(json_content):
    print(json.dumps(
        json_content,
        indent=4,
        sort_keys=True,
        ensure_ascii=False,
    ))


if __name__ == '__main__':

    try:
        filepath = argv[1]
        if os.path.isfile(filepath):
            pretty_print_json(load_data(filepath))
        else: 
            print('File not found')
    except ValueError:
        print('Invalid argument value')



