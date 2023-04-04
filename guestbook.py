guestbook = []

def display_menu():
    print("Guestbook menu:")
    print("1.Add a note")
    print("2.Edit a note")
    print("3.Delete a note")
    print("4.View guestbook")
    print("5.Exit")

def add_note():
    note=input("Enter note:")
    guestbook.append(note)
    print("Successfully added")

def edit_note():
    if len(guestbook) == 0:
        print("Guestbook is empty")
        return
    index = int(input("Enter the index of the note you want to edit:"))
    if index >= len(guestbook) or index < 0:
        print("Invalid Index")
        return
    new_note = input("Enter the new note")
    guestbook[index] = new_note
    print("Note updated successfully")

def delete_note():
    if len(guestbook) == 0:
        print("Guestbook is empty")
        return
    index=int(input("Enter the index you want to delete:"))
    if index >= len(guestbook) or index < 0:
        print("invalid index")
        return
    del guestbook[index]
    print("note deleted successfully")

def view_guestbook():
    print("Guestbook")
    for i, note in enumerate(guestbook):
        print(f"{i}. {note}")

while True:
    display_menu()
    choice = input("Enter your choice:")
    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        view_guestbook()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("invalid choice")
    





