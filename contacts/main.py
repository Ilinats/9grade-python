from contacts import PhoneBook 

phone_book = PhoneBook()
phone_book.add_contact("Boris", "Ivanov", "0886424423")
phone_book.add_contact("Petar", "Georgiev", "0899122356")
phone_book.add_contact("Gosho", "Iliev", "0893122656")
phone_book.add_contact("Alex", "Tsvestkov", "0888152349")
phone_book.update_phone_number("Petar", "Georgiev", "0888150457")
phone_book.remove_contact("Alex", "Tsvestkov")
phone_book.save_to_file("phonebook.json")
phone_book.load_from_file("phonebook.json")
print(phone_book)