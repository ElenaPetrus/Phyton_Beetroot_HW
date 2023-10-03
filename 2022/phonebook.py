import json

phonebook = {
    "+380972915744": {
        "first_name": "Roman",
        "second_name": "ABC",
        "city": "Washington DC",
        "state": "Columbia"
    },
    "56789087678909": {
        "first_name": "Adrian",
        "second_name": "ABC",
        "city": "Queens",
        "state": "New York",
    },
    "67876764543": {
        "first_name": "Serap",
        "second_name": "ABC",
        "city": "Washington DC",
        "state": "Columbia"
    },
    "65676545434": {
        "first_name": "Linus",
        "second_name": "ABC",
        "city": "Washington DC",
        "state": "Columbia"
    },
    "878007678755588": {
        "first_name": "Olena",
        "second_name": "Petrus",
        "city": "Washington DC",
        "state": "Columbia",
    },
}

new_list = []
for item in range(10):
    new_list.append(item**2)

new_list = [item**2 for item in range(10)]

new_dict = {}
for item in range(10):
    new_dict[item] = item**2

new_dict = {item: item**2 for item in range(10)}


def ask_user_info(answers=("first_name", "second_name", "city", "state")):
    return {
        answer: input(f"Write {answer} here please: ")
        for answer in answers
    }


def add(number):
    phonebook[number] = ask_user_info()


def update(number):
    phonebook[number].update(ask_user_info())


def delete(number):
    del phonebook[number]


actions = {
    1: delete,
    2: add,
    3: update,
}
actions_to_print = {key: action.__name__ for key, action in actions.items()}
print("Available actions are:")
print(json.dumps(actions, indent=4))
action = input("Please say what you want to do: ")
number = input("Please type the number: ")


actions[int(action)](number)

with open("phonebook.txt", "w+") as file:
    json.dump(phonebook, file)
    file.seek(0)

    new_phonebook = json.load(file)
    print(new_phonebook)
