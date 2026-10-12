import unittest

import contact_manager
from contact_manager import DuplicateContactError


class TestContactManager(unittest.TestCase):
    def setUp(self):
        # Clear the contacts dictionary before each test
        contact_manager.contacts.clear()

    def test_add_contact_success(self):
        contact_manager.add_contact("Alice", "12345")
        self.assertIn("Alice", contact_manager.contacts)
        self.assertEqual(contact_manager.contacts["Alice"], "12345")

    def test_add_duplicate_contact(self):
        contact_manager.add_contact("Bob", "67890")
        with self.assertRaises(DuplicateContactError):
            contact_manager.add_contact("Bob", "11111")

    def test_find_existing_contact(self):
        contact_manager.add_contact("Charlie", "54321")
        number = contact_manager.find_contact("Charlie")
        self.assertEqual(number, "54321")

    def test_find_nonexistent_contact(self):
        number = contact_manager.find_contact("David")
        self.assertIsNone(number)

    def test_delete_existing_contact(self):
        contact_manager.add_contact("Eve", "98765")
        contact_manager.delete_contact("Eve")
        self.assertNotIn("Eve", contact_manager.contacts)

    def test_delete_nonexistent_contact(self):
        # Ensure no exception is raised when deleting a non-existent contact
        try:
            contact_manager.delete_contact("Frank")
        except KeyError:
            self.fail("delete_contact raised KeyError unexpectedly!")


if __name__ == "__main__":
    unittest.main()



    