import json
from sys import argv

def load_data(filepath):
    with open(filepath) as myfile:
        return json.loads(myfile.read())


def pretty_print_json(json_file):
    print(json.dumps(json_file, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
   
    pretty_print_json(load_data(argv[1]))
