import json

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, first_name, last_name, phone_number):
        name = f"{first_name} {last_name}"
        self.contacts[name] = phone_number

    def update_phone_number(self, first_name, last_name, new_phone_number):
        name = f"{first_name} {last_name}"
        if name in self.contacts:
            self.contacts[name] = new_phone_number

    def remove_contact(self, first_name, last_name):
        name = f"{first_name} {last_name}"
        if name in self.contacts:
            del self.contacts[name]

    def __str__(self):
        output = ""
        for name, phone_number in self.contacts.items():
            output += f"{name}: {phone_number}\n"
        return output

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.contacts, f)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            self.contacts = json.load(f)
