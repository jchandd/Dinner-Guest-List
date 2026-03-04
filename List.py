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
    # Ask for list name then return
    return input("Enter Guest List: ").title().strip()


def add_guest():
    # Adds Guest to the list
    name = input("Enter Guest name: ").title().strip()

    guest_lists.append(name)  # Element to add to list


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
