import sys

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
    note = sys.argv[2]
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
        print("Guestbook is empty")
    else:
        list_notes()
        index = int(sys.argv[2])
        try:
            guestbook.pop(index-1)
            write_guestbook(guestbook)
            print("Note deleted successfully")
        except IndexError:
            print("Invalid Index")

def edit_note():
    if not guestbook:
        print("Guestbook is empty")
    else:
        list_notes()
        index = int(sys.argv[2])
        try:
            note_index = index - 1
            if note_index < 0 or note_index >= len(guestbook):
                print("Invalid text")
                return

            existing_note = guestbook[note_index]
            new_note = sys.argv[3]
            updated_note = f"{existing_note} {new_note}"
            guestbook[note_index] = updated_note
            write_guestbook(guestbook)
            print("Note edited successfully")
        except IndexError:
            print("Invalid Index")

guestbook = read_guestbook()

if sys.argv[1] == 'new':
    new_note()

elif sys.argv[1] == 'list':
    list_notes()

elif sys.argv[1] == 'delete':
    delete_note()

elif sys.argv[1] == 'edit':
    edit_note()

else:
    print(f"Invalid command: {sys.argv[1]}")
    sys.exit(1)