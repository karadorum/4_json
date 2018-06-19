import json


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as file:
            try:
                parsed_data = json.load(file)
                return parsed_data
            except json.JSONDecodeError:
                print('file must be json')
    except FileNotFoundError:
        print('file not found')


def pretty_print_json(raw_data):
    prettyfied_text = json.dumps(raw_data, indent=4, sort_keys=True)
    print(prettyfied_text)


if __name__ == '__main__':
    filepath = input('Enter filepath: ')
    pretty_print_json(load_data(filepath))
