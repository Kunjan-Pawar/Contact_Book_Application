# Contact Book Application

#empty dictionary to store contacts
contacts = {}

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count of contacts")
    print("7. Exit")

    choice = int(input("Choose an option (1-7): "))

    if choice == 1:
        name = input("Enter contact name: ")
        if name in contacts:
            print("Contact name {name} already exists.")
        else:
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            address = input("Enter contact address: ")
            contacts[name] = {"phone": phone, "email": email, "address": address}
            print(f"Contact name {name} added successfully.")

    elif choice == 2:
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact=contacts[name]
            print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:   
            print(f"Contact name {name} not found.")

    elif choice == 3:
        name = input("Enter contact name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contacts[name] = {"phone": phone, "email": email, "address": address}
            print(f"Contact name {name} updated successfully.")
        else:
            print(f"Contact name {name} not found.")

    elif choice == 4:
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} deleted successfully.")
        else:
            print(f"Contact name {name} not found.")

    elif choice == 5:
        search_name = input("Enter contact name to search: ")
        found = False          #flag to check if any contact is found
        for name, contact in contacts.items():            #loop through all contacts
            if search_name.lower() in name.lower():          #case insensitive search
                print(f"Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
                found = True             #set flag to true if contact is found
        if not found:
            print(f"No contacts found matching {search_name}.")

    elif choice == 6:
        print(f"Total contacts: {len(contacts)}")

    elif choice == 7:
        print("Exiting Contact Book. Goodbye!")
        break   
    else:
        print("Invalid choice.")
