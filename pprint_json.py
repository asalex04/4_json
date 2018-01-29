import json


def load_data(filepath):
    with open(filepath) as myfile:
        return json.loads(myfile.read())


def pretty_print_json(jstxt):
    print(json.dumps(jstxt, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    jstxt = load_data(input("path to file: "))
    pretty_print_json(jstxt)
