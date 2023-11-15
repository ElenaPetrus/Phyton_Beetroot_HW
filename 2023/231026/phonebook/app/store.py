import json

# Each phonebook in format: {'fist_name': Olena, 'last_name': Petrus, 'number': +380675634383, 'city': Dnipro,  }
phonedata = []


def load_phonedata(filename='store.json'):
    global phonedata

    try:
        with open(filename, 'r') as f:
            phonedata = json.load(f)

        if not phonedata:
            phonedata = []
    except FileNotFoundError:
        print(
            '"Warning: {filename} does not exist.')


def save_phonedata(filename='store.json'):
    with open(filename, 'w') as f:
        json.dump(phonedata, f, indent=2)
