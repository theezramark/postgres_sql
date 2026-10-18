import database

menu = """ 
Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to the programming diary!"

# Functionality
def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    database.add_entry(entry_content, entry_date)
    print("Adding...")
    print("Added")

def view_entries(entries):
    print("===viewing entries===")
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n")

print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(database.get_entries())
    else:
        print("Invalid option, please try again!")
