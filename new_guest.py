guestbook = []

def display_menu():
    print("+--------------------------------------------+")
    print("|            Guestbook menu:                 |")
    print("+--------------------------------------------+")
    print("|  1. Add a note by typing 1                 |")
    print("|  2. Edit a note by typing edit <index>     |")
    print("|  3. Delete a note by typing delete <index> |")
    print("|  4. List notes by typing list              |")
    print("|  5. Exit by typing 5                       |")
    print("|  6. Bring back menu by typing menu         |")
    print("+--------------------------------------------+")

def add_note(note=None):
    if note is None:
        note = input("Enter note:")
    guestbook.append(note)
    print("Note added successfully")

def edit_note(index):
    if len(guestbook) == 0:
        print("Guestbook is empty")
        return
    if index >= len(guestbook) or index < 0:
        print("Invalid Index")
        return
    new_note = input("Enter the new note:")
    guestbook[index] = new_note
    print("Note updated successfully")

def delete_note(index):
    if len(guestbook) == 0:
        print("Guestbook is empty")
        return
    if index >= len(guestbook) or index < 0:
        print("Invalid Index")
        return
    del guestbook[index]
    print("Note deleted successfully")

def list_notes():
    if len(guestbook) == 0:
        print("Guestbook is empty")
        return
    print("These are my notes:")
    for i, note in enumerate(guestbook):
        print(f"{i}. {note}")

display_menu_flag = True

while True:
    if display_menu_flag:
        display_menu()
    choice = input("Enter your choice:")
    if choice == "1":
        add_note()
    elif choice.startswith("new "):
        note = choice.split(" ", 1)[1]
        add_note(note)
    elif choice.startswith("edit"):
        index = int(choice.split()[1])
        edit_note(index)
    elif choice.startswith("delete"):
        index = int(choice.split()[1])
        delete_note(index)
    elif choice.lower() == "list":
        list_notes()
    elif choice == "5":
        print("Goodbye")
        break
    elif choice.lower() == "menu":
        display_menu_flag = True
    else:
        print("Invalid choice")

    # set the display_menu_flag to False to prevent the menu from being displayed again
    if not display_menu_flag:
        continue

    # check if the user entered 6 to bring back the menu
    if choice == "menu":
        display_menu_flag = True
    else:
        display_menu_flag = False
