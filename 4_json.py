import json
import sys


def load_data(filepath): 
    with open(filepath, encoding='utf-8') as file:   
        parsed_data = json.load(file)
        return parsed_data
            


def pretty_print_json(data):
    prettyfied_text = json.dumps(data, indent=4, sort_keys=True)
    print(prettyfied_text)


if __name__ == '__main__':
    
    try:
        pretty_print_json(load_data(sys.argv[1]))
    except json.JSONDecodeError:
        print('file must be json')
    except FileNotFoundError:
        print('file not found')
