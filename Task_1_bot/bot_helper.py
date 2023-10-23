def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please.\n"
        except IndexError:
            return "Index out of bounds or does not exist"
        except KeyError as ke:
            return f"This contact {ke} does not exist"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added.\n"

@input_error
def change_contact(name, phone, contacts):
    if name not in contacts:
        return "Contact not found.\n"
    else:
        contacts[name] = phone
        return "Contact updated.\n"

@input_error
def show_phone(name, contacts):
    if name not in contacts:
        return "Contact not found.\n"
    else:
        return contacts[name]

@input_error
def print_contacts(contacts):
    if not contacts:
        return "No contacts.\n"
    for name, phone in contacts.items():
        print(f"{name}: {phone}\n")

def main():
    contacts = {}
    print("Welcome to the assistant bot!\n")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?\n")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(*args, contacts))
        elif command == "phone":
            print(show_phone(args[0], contacts))
        elif command == "all":
            print_contacts(contacts)
        else:
            print("Invalid command.\n")

if __name__ == "__main__":
    main()