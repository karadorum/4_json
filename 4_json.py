import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        parsed_data = json.load(file)
        return parsed_data


def pretty_print_json(json_data):
    prettyfied_json = json.dumps(json_data, indent=4, sort_keys=True)
    print(prettyfied_json)


def get_arg(arg):
    try:
        arg_data = load_data(arg)
    except json.JSONDecodeError:
        exit('file must be json')
    except FileNotFoundError:
        exit('file not found')
    except IndexError:
        exit('name of file argument is empty')
    return arg_data


if __name__ == '__main__':

    pretty_print_json(get_arg(sys.argv[1]))
