def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found..."
        except IndexError:
            return "Enter a valid command with necessary arguments."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name.capitalize()] = phone
        return "Contact added."
    return 'Contact already exists.'

@input_error    
def change_contact(args, contacts):
    name, phone = args
    name = name.capitalize()
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return 'Contact not found.'

@input_error
def show_phone(args, contacts):
    name = args[0].capitalize()
    if name in contacts:
        return contacts[name]
    return 'Contact not found.'

def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f'{name}: {phone}')
    else:
        print("No contacts yet.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case 'exit' | 'close':
                print("Good bye!")
                break
            case 'hello':
                print("How can I help you?")
            case 'add': 
                print(add_contact(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'phone':
                print(show_phone(args, contacts))
            case "all":
                show_all(contacts)
            case _:
                print("Invalid command.")
    
if __name__ == "__main__":
    main()

