import json
from sys import argv
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding='utf-8') as myfile:
        return json.loads(myfile.read())


def pretty_print_json(data_dictionary):
    print(json.dumps(data_dictionary, sort_keys=True,
                     indent=4, ensure_ascii=False))


if __name__ == '__main__':

    pretty_print_json(load_data(argv[1]))
