import os
import sys
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="Phonebook file path")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))

PHONEBOOK = {}

datafile_path = os.path.join(current_dir, (args.data_path + ".json"))


def user_exit():
    sys.exit()


def create_contact():
    response = input("You are in 'creating a contact' mode, if you like to exit press 'x'/'X' and Enter keys.\n If you want to continue press Enter key\n")
    if response == "x" or response == "X":
        user_exit()
    first_name = input("Please, input your first name:  ")
    last_name = input("Please, input your last name:  ")
    full_name = last_name + " " + first_name
    phone_number = input("Please, input your telephone number:  ")
    location = input("Please, input your location information (city/state/district):  ")

    if phone_number and full_name and location:
        PHONEBOOK[phone_number] = {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "location": location,
        }
    else:
        print("Unable to create a contact. Your input is not valid.")
        user_exit()


def search_by_first_name(first_name):
    results = [contact for contact in PHONEBOOK.values() if contact["first_name"].lower() == first_name.lower()]
    return results


def search_by_last_name(last_name):
    results = [contact for contact in PHONEBOOK.values() if contact["last_name"].lower() == last_name.lower()]
    return results


def search_by_full_name(full_name):
    results = [contact for contact in PHONEBOOK.values() if full_name.lower() in contact["full_name"].lower()]
    return results


def search_by_telephone_number(phone_number):
    contact = PHONEBOOK.get(phone_number)
    return [contact] if contact else []


def search_by_location(location):
    results = [contact for contact in PHONEBOOK.values() if location.lower() in contact["location"].lower()]
    return results


def delete_contact(phone_number):
    if phone_number in PHONEBOOK:
        del PHONEBOOK[phone_number]
        return "Contact successfully was deleted."
    else:
        return "Unable to delete contact."
        user_exit()


def update_contact(phone_number, updated_data):
    if phone_number in PHONEBOOK:
        PHONEBOOK[phone_number].update(updated_data)
        return "Contact successfully updated"
    else:
        return "Unable to update contact, check your input info"
        user_exit()


if os.path.exists(datafile_path):
    with open(datafile_path, "r") as file_object:
        PHONEBOOK = json.load(file_object)

create_contact()

with open(datafile_path, "w") as file_object:
    json.dump(PHONEBOOK, file_object, indent=4)
    print(PHONEBOOK)
    response = input("You successfully created new contact, if you like to exit press 'x'/'X' and Enter keys.\n")
    if response == "x" or response == "X":
        user_exit()
