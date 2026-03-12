guest_invitations = []
guest_lists = []


def make_dinnerlist():
    while True:
        name = input("\nEnter Guest List Name: ").strip().title()

        if name == "":
            print("\nList name cannot be empty.")
        else:
            print("\nDinner list created:", name)
            return name


def add_guest():
    name = input("Enter Guest name: ").strip().title()

    if name == "":
        print("\nName can't be empty")
        return

    if name in guest_lists:
        print("\nDuplicate name error")
        return

    invite = input("\nEnter number of invites: ").strip()

    if not invite.isdigit():
        print("\nInvite must be a number")
        return

    guest_lists.append(name)
    guest_invitations.append(int(invite))

    print("\nGuest added successfully.")


def remove_guest():
    name = input("\nWhich guest would you like to remove? ").strip().title()
    if name in guest_lists:
        index = guest_lists.index(name)
        guest_lists.pop(index)
        guest_invitations.pop(index)
        print("Guest removed.")
    else:
        print("\nNo known guest on list.")


def modify_guest():
    name = input("\nEnter guest name to make changes: ").strip().title()
    if name not in guest_lists:
        print("\nNo guest by that name.")
        return

    index = guest_lists.index(name)

    new_name = input("\nEnter new name: ").strip().title()

    if new_name == "":
        print("\nName can't be empty")
        return

    if new_name in guest_lists and new_name != name:
        print("\nDuplicate names not allowed")
        return

    invite = input("\nEnter new invitations: ").strip()

    if not invite.isdigit():  # means the input is not a number
        print("\nInvite must be numerical")
        return

    guest_lists[index] = new_name
    guest_invitations[index] = int(invite)

    print("\nGuest has been modified.")


def show_guests():
    if not guest_lists:
        print("\nNo guests in list")
        return

    print("\nDinner Guest List")
    for i in range(
        len(guest_lists)
    ):  # goes through the guest list and prints the name and number of invitations for each guest
        print(guest_lists[i], "-", guest_invitations[i])


def show_invitations():
    if not guest_lists:
        print("\nNo invitations in list")
        return

    print("\nDinner Guest Invitations")

    for i in range(len(guest_lists)):
        print(
            guest_lists[i], "-", guest_invitations[i]
        )  # goes through the guest list and prints the name and number of invitations for each guest

    print("\nTotal Guests:", len(guest_lists))


    for index in range(len(guest_invitations)):

     print(guest_invitations[index])

    print(guest_lists[index], "-", guest_invitations[index])



def sort_guests():
    if not guest_lists:
        print("\nNo guests in list")
        return

    sorted_guests = sorted(zip(guest_lists, guest_invitations))
    guest_lists[:], guest_invitations[:] = zip(
        *sorted_guests
    )  # sorts the guest list and the invitations together based on the guest names

    print("\nGuests sorted alphabetically.")


def show_guestcount():
    print("\nNumber of guests:", len(guest_lists))


def main():
    make_dinnerlist()

    while True:
        print("\nDinner Guest List Menu")
        print("1. Add Guest")
        print("2. Modify Guest")
        print("3. Remove Guest")
        print("4. Sort Guests")
        print("5. Number of Guests")
        print("6. Show Invites")
        print("7. Show Guest List")
        print("8. Exit")

        choice = input("Enter Choice: ").strip()

        if choice == "":
            print("Please enter a number between 1 and 8.")
            continue

        if choice == "1":
            add_guest()
        elif choice == "2":
            modify_guest()
        elif choice == "3":
            remove_guest()
        elif choice == "4":
            sort_guests()
        elif choice == "5":
            show_guestcount()
        elif choice == "6":
            show_invitations()
        elif choice == "7":
            show_guests()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Select a valid option.")


if __name__ == "__main__":
    main()
