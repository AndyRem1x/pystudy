import json
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="Name of Phonebook")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(current_dir, args.file_name + ".json")
temp_file = os.path.join(current_dir, "temp.json")
mock_file = os.path.join(current_dir, "mock", "phonebook_mock_data.json")


class PhoneBook:
    """Phonebook class"""

    def __init__(self, file_path, temp_file_path, mock_file_path=None):
        self.file_path = file_path
        self.temp_path = temp_file_path
        self.mock_path = mock_file_path

        # Initialization for empty phonebook file
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="UTF-8") as file:
                file.write("{}")

    def open_file(self):
        """Open phonebook file to read"""
        try:
            with open(self.file_path, "r", encoding="UTF_8") as book_file:
                return json.load(book_file)
        except FileNotFoundError:
            print(f'Error! File with name "{self.file_path}" not found!')
        return None

    def create_backup_file(self):
        """Create backup file"""
        os.replace(self.file_path, self.temp_path)

    def backup_phonebook(self, backup_file=None):
        """Rewrite phonebook file from backup file"""
        try:
            with open(backup_file, "r", encoding="UTF_8") as file_obj:
                temp_data = json.load(file_obj)
            with open(self.file_path, "w", encoding="UTF_8") as book_file:
                json.dump(temp_data, book_file, indent=4)
            return True
        except FileNotFoundError:
            print("Error: Backup file not exist")
            return False

    def save_phonebook_to_file(self, phonebook):
        """Convert object phonebook to json format and save it to file"""
        try:
            with open(self.file_path, "w", encoding="UTF_8") as book_file:
                json.dump(phonebook, book_file, indent=4)
        except Exception:
            print("Rewrite error!")
            self.backup_phonebook(self.temp_path)

    def show_all(self):
        """Show all entries in phonebook"""
        try:
            with open(self.file_path, "r", encoding="UTF_8") as book_file:
                print(book_file.read())
        except FileNotFoundError:
            print(f'Error! File with name "{self.file_path}" not found!')

    def add(self, contact_details):
        """
        Add new entries.
        Return True if operation completed successful, and False in another case.
        """
        phonebook = self.open_file()

        if contact_details["phone"] in phonebook:
            print(
                f"Contact with phone number {contact_details['phone']} is already exist!"
            )
            operation_code = input("Do you want to update this data? (y/n): ")
            if not operation_code == "y":
                return False

        # create new contact
        phonebook[f"{contact_details['phone']}"] = {
            "first_name": contact_details["first_name"],
            "last_name": contact_details["last_name"],
            "location": contact_details["location"],
        }

        # create backup file
        self.create_backup_file()

        # update phonebook
        self.save_phonebook_to_file(phonebook)

        return True

    def search_by(self, key, value):
        """Search contact by key and its value"""
        phonebook = self.open_file()
        contacts = []

        match key:
            case "phone":
                if value not in phonebook:
                    return None
                data = phonebook[value]
                data["phone"] = value
                contacts.append(data)
            case "full_name":
                for contact, data in phonebook.items():
                    if (
                        value.lower()
                        == f"{data['first_name']} {data['last_name']}".lower()
                    ):
                        data["phone"] = contact
                        contacts.append(data)
                    continue
            case _:
                for contact, data in phonebook.items():
                    if value.lower() == data[key].lower():
                        data["phone"] = contact
                        contacts.append(data)
                    continue

        return contacts if len(contacts) > 0 else None

    def update_by_phone(self, phone, new_data):
        """
        Update a record for a given telephone number.
        Return True if operation completed successful, and False in another case.
        """
        phonebook = self.open_file()

        if phone not in phonebook:
            print(f"Contact with phone number {phone} not found.")
            return False

        # update data
        phonebook[f"{phone}"] = {
            "first_name": new_data["first_name"],
            "last_name": new_data["last_name"],
            "location": new_data["location"],
        }

        # create backup file
        self.create_backup_file()

        # update phonebook
        self.save_phonebook_to_file(phonebook)

        return True

    def delete_by_phone(self, phone):
        """
        Delete a record for a given telephone number
        Return True if operation completed successful, and False in another case.
        """
        phonebook = self.open_file()
        if phone not in phonebook:
            print(f"Contact with phone number {phone} not found!")
            return False
        del phonebook[phone]
        self.save_phonebook_to_file(phonebook)
        return True

    def interface(self):
        """Main function loop"""

        while True:
            print(
                "\n",
                "What do you want to do?",
                "1. Add contact",
                "2. Search by first name",
                "3. Search by last name",
                "4. Search by full name",
                "5. Search by phone number",
                "6. Search by location",
                "7. Update contact by phone number",
                "8. Delete contact by phone number",
                "9. Show all contacts in phonebook",
                "10. Backup phonebook from Mock_data",
                "Enter 'q' to quit",
                sep="\n",
            )
            operation_code = input("Enter the code: ")

            match operation_code:
                case "1":
                    contact_details = {}
                    print("Please, enter the details for creating new contact:")
                    contact_details["first_name"] = input("Enter first name: ")
                    contact_details["last_name"] = input("Enter last name: ")
                    contact_details["phone"] = input("Enter phone number: ")
                    contact_details["location"] = input("Enter city or state: ")
                    success = self.add(contact_details)
                    if success:
                        print("The Phonebook successfully updated!")
                case "2":
                    user_value = input("Search contact(s) by first name: ")
                    print(
                        self.search_by("first_name", user_value)
                        or "Contact(s) not found!"
                    )
                case "3":
                    user_value = input("Search contact(s) by last name: ")
                    print(
                        self.search_by("last_name", user_value)
                        or "Contact(s) not found!"
                    )
                case "4":
                    user_value = input("Search contact(s) by full name: ")
                    print(
                        self.search_by("full_name", user_value)
                        or "Contact(s) not found!"
                    )
                case "5":
                    user_value = input("Search contact(s) by phone number: ")
                    print(
                        self.search_by("phone", user_value) or "Contact(s) not found!"
                    )
                case "6":
                    user_value = input("Search contact(s) by location: ")
                    print(
                        self.search_by("location", user_value)
                        or "Contact(s) not found!"
                    )
                case "7":
                    phone = input("Enter phone number: ")

                    new_data = {}
                    print("Please, enter the details for updating contact:")
                    new_data["first_name"] = input("Enter first name: ")
                    new_data["last_name"] = input("Enter last name: ")
                    new_data["location"] = input("Enter city or state: ")

                    success = self.update_by_phone(phone, new_data)
                    if success:
                        print("The Phonebook successfully updated!")
                case "8":
                    phone = input("Enter phone number: ")
                    success = self.delete_by_phone(phone)
                    if success:
                        print("The contact successfully deleted!")
                case "9":
                    self.show_all()
                case "10":
                    success = self.backup_phonebook(self.mock_path)
                    if success:
                        print("The Phonebook successfully updated!")
                case "q":
                    sys.exit()
                case _:
                    print("Unknown code. Try again")
                    continue
            input("Press 'Enter' to continue.")


my_phonebook = PhoneBook(file_name, temp_file, mock_file)
