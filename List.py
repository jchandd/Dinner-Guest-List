# Dinner Guest List Requirements:
# 1. Add guest.
# 2. Modify guest.
# 3. Remove guest.
# 4. Sort guests.
# 5. Show number of guests.
# 6. Show invitations.

# Please make sure to have some validation so the app doesn't break
# when someone enters empty string and make sure strings are formatted nicely at input
# Make sure there are no duplicate names!
# Reject names if there are duplicates

guest_invitations = []
guest_lists = []


def make_dinnerlist():
    while True:
        name = input("Enter Guest List: ").strip().title()
        if name == "": # Code to avoid empty list name
            print("List name is empty")
        else:
            return name
    

def add_guest():
    # Adds Guest to the list
    name = input("Enter Guest name: ").title().strip()

    if name == "": # Code for empty name
        print("Name can't be empty")
        return
    
    if name in guest_lists:
        print("Duplicate name error")
        return
    
    invite = input("Enter number of invites:").strip()

    if not invite.isdigit():
        print("Invite must be number")
        return
    
    guest_lists.append(name) # Append= Add element
    guest_invitations.append(int(invite))
    print("Added guest")

def remove_guest():
    # Removes guest and their invite
    name = input("Which guest would you like to remove?").title().strip()

    # Check name is in dinner list

    # If in list remove, if not print message
    if name in guest_lists:  # Checks if names are in list
        index = guest_lists.index(name)  # Get index of name entered
        guest_lists.pop(index)  # Pops or removes Guest
        guest_invitations.pop(index)  # Removes guest invitation
    else:
        print("No known guest on list.")

def modify_guest():
    name = input("Enter guest name to make changes:").title().strip()

    if name not in guest_lists:
        print("No guest by that name")
        return
    
    index = guest_lists.index(name)

    new_name = input("Enter new name:").strip().title()

    if new_name == "":
        print("Can't have empty name")
        return
    
    if new_name in guest_lists and not new_name == name:
        print("Duplicate names not allowed")
        return
    
    invite = input("Enter new invitations:").strip()

    if not invite.isdigit(): # is.digit literally means if there is digits
        print("Invite must be1 numerical")
        return
    
    guest_lists[index] = new_name
    guest_invitations[index] = int(invite)

    print("Guest has been modified")




def show_guests():
    # Show all guests
    if not guest_lists:
        print("No guests in list")
        return
    # Go through list of guests.
    print("\nDinner Guest List")
    for index in range(len(guest_lists)):
        print(guest_lists[index], "-", guest_invitations[index])


def show_invitations():
    # Show all invitations
    if not guest_invitations:
        print("No invitations in list")
        return
    # Go through list of guests.
    print("\nDinner Guest Invitations")
    for index in range(len(guest_invitations)):
        print(guest_invitations[index])

def sort_guests():
    if not guest_lists:
        print("No Guests to sort")
        return
    
    combined = list(zip(guest_lists, guest_invitations))
    combined.sort()

    guest_lists.clear()
    guest_invitations.clear()

    for name, invite in combined:
        guest_lists.append(name)
        guest_invitations.append(invite)

    print("Sorted guests")

def show_guestcount():
    print("Guest number:", len(guest_lists))  

def main():
    list_name = make_dinnerlist()

    while True:
        print("\nDinner Guest List:", list_name)
        print("1. Add Guest")
        print("2. Modify Guest")
        print("3. Remove Guest")
        print("4. Sort Guest")
        print("5. Number of Guests")
        print("6. Show Invites")
        print("7. Show guest lists")
        print("8. Leave")

        choice = input("Enter Choice: ").strip()

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
            print("Goodbye")
            break
        else:
            print("Select valid option")


if __name__ == "__main__":
    main()