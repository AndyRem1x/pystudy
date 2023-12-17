import json
import unittest
import os
from phonebook import PhoneBook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.file_path = os.path.join(current_dir, "phonebookTest.json")
        self.temp_path = os.path.join(current_dir, "temp.json")
        self.mock_path = os.path.join(current_dir, "mock", "mockfile.json")
        with open(self.mock_path, "r", encoding="UTF_8") as mock_file:
            self.mock_data = json.load(mock_file)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="UTF-8") as file:
                file.write("{}")

        self.phone_book = PhoneBook(self.file_path, self.temp_path, self.mock_path)
        self.new_entry = {
            "first_name": "Sarah",
            "last_name": "Connor",
            "location": "Los Angeles, California",
            "phone": "+1-213-978-2222",
        }

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.temp_path):
            os.remove(self.temp_path)

    def test_add(self):
        self.phone_book.add(self.new_entry)
        new_contact = {
            self.new_entry["phone"]: {
                "first_name": self.new_entry["first_name"],
                "last_name": self.new_entry["last_name"],
                "location": self.new_entry["location"],
            }
        }
        base = self.phone_book.open_file()
        self.assertEqual(base, new_contact)

    def test_save_phonebook_to_file(self):
        self.phone_book.save_phonebook_to_file(self.mock_data)
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)

    def test_search_by_phone(self):
        self.phone_book.backup_phonebook(self.mock_path)
        result = self.phone_book.search_by('phone', "+1-213-978-5555")
        self.assertEqual(result, None)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('phone', self.new_entry['phone'])
        self.assertEqual(result, [self.new_entry])

    def test_search_by_first_name(self):
        self.phone_book.backup_phonebook(self.mock_path)
        result = self.phone_book.search_by('first_name', "Sarah")
        self.assertEqual(result, None)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('first_name', "Sarah")
        self.assertEqual(result, [self.new_entry])

    def test_search_by_last_name(self):
        self.phone_book.backup_phonebook(self.mock_path)
        result = self.phone_book.search_by('last_name', "Connor")
        self.assertEqual(result, None)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('last_name', "Connor")
        self.assertEqual(result, [self.new_entry])

    def test_search_by_full_name(self):
        self.phone_book.backup_phonebook(self.mock_path)
        result = self.phone_book.search_by('full_name', "Sarah Connor")
        self.assertEqual(result, None)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('full_name', "Sarah Connor")
        self.assertEqual(result, [self.new_entry])

    def test_search_by_location(self):
        self.phone_book.backup_phonebook(self.mock_path)
        result = self.phone_book.search_by('location', "Los Angeles, California")
        self.assertEqual(result, None)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('location', "Los Angeles, California")
        self.assertEqual(result, [self.new_entry])

    def test_delete_by_phone(self):
        self.phone_book.backup_phonebook(self.mock_path)
        self.phone_book.delete_by_phone("+1-213-978-5555")
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)
        self.phone_book.add(self.new_entry)
        self.phone_book.delete_by_phone(self.new_entry["phone"])
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)

    def test_update_by_phone(self):
        self.phone_book.add(self.new_entry)
        new_data = {
            "first_name": self.new_entry["first_name"],
            "last_name": "Reese",
            "location": self.new_entry["location"],
        }
        self.phone_book.update_by_phone(self.new_entry["phone"], new_data)
        new_contact = {self.new_entry["phone"]: new_data}

        base = self.phone_book.open_file()
        self.assertEqual(base, new_contact)

    def test_backup_phonebook(self):
        self.phone_book.save_phonebook_to_file(self.mock_data)
        self.phone_book.create_backup_file()
        self.phone_book.save_phonebook_to_file({})
        base = self.phone_book.open_file()
        self.assertEqual(base, {})
        self.phone_book.backup_phonebook(self.temp_path)
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)


if __name__ == "__main__":
    unittest.main()
