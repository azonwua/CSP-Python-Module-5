# CSP-Python-Module-5
# Contact Manager CLI

A robust command-line contact management application written in Python, featuring strict input validation, custom error handling, and a full unit test suite written with Python's 'unittest' framework.

---

## Features

- **Add Contacts:** Save new contact names and phone numbers. Prevents duplicates using a custom exception.
- **Find Contacts:** Look up existing contact numbers gracefully without key error crashes.
- **Delete Contacts:** Remove contacts safely with user feedback.
- **Input Validation:** Handles non-integer menu input smoothly using 'try/except' blocks.
- **Unit Tested:** Built following Test-Driven Development (TDD) principles to cover success and error states.

---

## Project Structure
.
├── contact_manager.py       # Main application logic and CLI interface
├── test_contact_manager.py  # Unit test suite using unittest
└── README.md                # Project documentation

--- Contact Manager ---
1. Add Contact
2. Find Contact
3. Delete Contact
4. Exit
Enter your choice: 1
Enter contact name: Alice
Enter phone number: 555-0199

--- Contact Manager ---
1. Add Contact
2. Find Contact
3. Delete Contact
4. Exit
Enter your choice: 2
Enter contact name: Alice
Enter phone number: 555-0199
Contact 'Alice' Found: 555-0199

https://youtu.be/dzejH-k6QBs
