# Custom exception for duplicate contacts
class DuplicateContactError(Exception):
    pass

# Shared dictionary storing contact names and numbers
contacts = {}


# Add a contact to the contacts dictionary
def add_contact(name, number):
    if name in contacts:
        raise DuplicateContactError(f"Contact '{name}' already exists.")
    contacts[name] = number
    print(f"Contact '{name}' added successfully.")


# Finds and returns a contact's phone number if it exists in the contacts dictionary
def find_contact(name):
    try:
        number = contacts[name]
        print(f"Contact '{name}' found: {number}")
        return number
    except KeyError:
        print(f"Contact '{name}' not found.")
        return None


# Deletes a contact from the contacts dictionary if it exists
def delete_contact(name):
    try:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    except KeyError:
        print(f"Contact '{name}' not found. Cannot delete.")


def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            try:
                add_contact(name, number)
            except DuplicateContactError as e:
                print(e)
        elif choice == '2':
            name = input("Enter contact name to find: ")
            find_contact(name)
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '4':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

            