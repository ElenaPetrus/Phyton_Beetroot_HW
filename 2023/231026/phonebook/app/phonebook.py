from app import store


def add_data():
    new_entry = {
        'first_name': input('Enter first name: '),
        'last_name': input('Enter last name: '),
        'number': input('Enter phone number: '),
        'city': input('Enter city or state: ')
    }
    store.phonedata.append(new_entry)
    store.save_phonedata()
    print("New contact is added successfully!")


def search_by_first_name(first_name):
    while True:
        try:
            first_name = input(
                "Enter the first name to search: ").strip().lower()

            if first_name.isalpha():
                break
            else:
                raise ValueError(
                    "Please enter a valid first name with only letters.")
        except ValueError as e:
            print(e)

    results = []

    for entry in store.phonedata:
        if entry['first_name'].lower() == first_name:
            results.append(entry)

    return results


def search_by_last_name(last_name):
    pass


def search_by_full_name(first_name, last_name):
    pass


def delete_record(number):
    for entry in store.phonedata:
        if entry['number'] == number:
            store.phonedata.remove(entry)
            print("Record deleted successfully!")
            return
    print("Record not found.")
