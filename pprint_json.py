import json


def load_data(filepath):
    with open(filepath) as myfile:
        return json.loads(myfile.read())


def pretty_print_json(data):
   print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    data = load_data(input("path to file: "))
    pretty_print_json(data)
