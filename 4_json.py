import json



def load_data():
    with open('alco_shops.json', encoding= 'utf-8') as file:
        parsed = json.load(file)
    return parsed
    

def pretty_print_json(data):
    s = json.dumps(data, indent = 4, sort_keys = True)
    with open('alco.txt', 'w') as f:
        f.write(s)

    


if __name__ == '__main__':
    pretty_print_json(load_data())