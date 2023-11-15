from settings import app_name, app_version
from app import phonebook, store


def main():
    store.load_phonedata()

    print(f"Welcome to {app_name}/{app_version}!")

    print("""
Please select action.
a - Add new entries
f - Search by first name
l - Search by last name
n - Search by full name
t - Search by telephone number
c - Search by city or state
d - Delete a record for a given telephone number
u - Update a record for a given telephone number
q - to quit from application""")

    while True:
        try:
            action = input("\nYour action: ")

            if action == 'q':
                print("See you next time")
                break

            elif action == 'a':
                phonebook.add_data()

            elif action == 'f':
                phonebook.search_by_first_name()

            elif action == 'l':
                phonebook.search_by_last_name()

            elif action == 'n':
                phonebook.search_by_full_name()

            elif action == 't':
                phonebook.search_by_number()

            elif action == 'c':
                phonebook.search_by_city()

            elif action == 'd':
                phonebook.delete_data()

            elif action == 'u':
                phonebook.update_data()
        except:
            print("Unexpected error! Please check your input or values.")


if __name__ == "__main__":
    main()
