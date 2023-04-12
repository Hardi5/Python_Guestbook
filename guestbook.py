import argparse

GUESTBOOK_FILE = "guestbook.txt"

def read_guestbook():
    try:
        with open(GUESTBOOK_FILE, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def write_guestbook(guestbook):
    with open(GUESTBOOK_FILE, "w") as f:
        f.write("\n".join(guestbook))

def new_note():
    note = input("Enter your note:" )
    guestbook.append(note)
    write_guestbook(guestbook)
    print("Note added successfully")

def list_notes():
    if not guestbook:
        print("Guestbook is empty.")
    else:
        for i, note in enumerate(guestbook):
            print(f"{i+1}. {note}")

def delete_note():
    if not guestbook:
        print("Gustbook is empty")
    else:
        list_notes()
        index = int(input("Enter the index of the note you want to delete: "))
        try:
            guestbook.pop(index-1)
            write_guestbook(guestbook)
            print("Note successfully deleted")
        except IndexError():
                print("Invalid Index")

def edit_note():
    if not guestbook:
        print("Guestbook is empty")
    else:
        list_notes()
        index = int(input("Enter the index of the note you want to edit: "))
        try:
            new_note = input("Enter the new note: ")
            guestbook[index-1] = new_note
            write_guestbook(guestbook)
            print("Note edited successfully")
        except IndexError:
            print("Invalid index")


parser = argparse.ArgumentParser(description="Guestbook CLI")
parser.add_argument('action', choices=['new', 'list', 'delete', 'edit'])
args = parser.parse_args()

guestbook = read_guestbook()

if args.action == 'new':
    new_note()
elif args.action == 'list':
    list_notes()
elif args.action == 'delete':
    delete_note()
elif args.action == 'edit':
    edit_note()