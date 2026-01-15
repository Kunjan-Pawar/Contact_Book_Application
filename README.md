# 📇 Contact Book

A simple command-line application to manage your contacts easily.

## What It Does

This Contact Book lets you store, organize, and manage all your contacts in one place. You can add phone numbers, email addresses, and physical addresses for each contact.

## Requirements

- Python 3.x

## Features

- **Add Contact** - Save a new contact with their name, phone number, email, and address
- **View Contact** - Look up a specific contact's information
- **Update Contact** - Change the details of an existing contact
- **Delete Contact** - Remove a contact from your book
- **Search Contact** - Find contacts by searching for part of their name
- **Count Contacts** - See how many contacts you have saved
- **Exit** - Close the application

## How to Use

1. **Run the program:**
   ```bash
   python contact_book.py
   ```

2. A menu will appear with 7 options (1-7)

3. Enter the number of the action you want to perform

4. Follow the prompts to enter contact information

5. Choose option 7 to exit the application

## Example

```
Contact Book Menu:
1. Add Contact
2. View Contacts
3. Update Contact
4. Delete Contact
5. Search Contact
6. Count of contacts
7. Exit

Choose an option (1-7): 1
Enter contact name: John Doe
Enter contact phone number: 555-1234
Enter contact email address: john@example.com
Enter contact address: 123 Main St
Contact name John Doe added successfully.
```

## Notes

- **Unique Names** - Contact names must be unique; you can't have two contacts with the same name
- **Case-Insensitive Search** - When searching, the search is case-insensitive (searching "john" will find "John")
- **Temporary Storage** - All your contacts are stored while the program is running, but they are lost when you exit (consider saving to a file for future improvements)

## Future Improvements

- Save contacts to a file (JSON/CSV)
- View all contacts at once
- Search by phone or email
- Contact categories
-SQLite for permanent Data Storage
-GUI Interface 