import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        parsed_data = json.load(file)
        return parsed_data


def pretty_print_json(json_data):
    prettyfied_json = json.dumps(json_data, indent=4, sort_keys=True)
    print(prettyfied_json)


if __name__ == '__main__':
    try:
        json_data = load_data(sys.argv[1])
    except json.JSONDecodeError:
        print('file must be json')
    except FileNotFoundError:
        print('file not found')
    except IndexError:
        print('name of file argument is empty')

    pretty_print_json(json_data)
