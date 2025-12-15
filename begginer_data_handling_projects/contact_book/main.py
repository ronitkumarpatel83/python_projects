import json

class ContactBook:
    def __init__(self):
        self.path = r"begginer_data_handling_projects\contact_book\contacts.json"

    def add_contact(self):
        name = input("Enter your name :")
        contact = input("Enter your phone no.: ")
        email = input("Enter your email : ")
        
        with open(self.path, 'a') as file:
            json.dump(name, contact, email)

    def search_contact(self):
        pass

    def delete_contact(self):
        pass

    def view_all_contact(self):
        pass


if __name__ == "__main__":
    print("="*120)
    print("="*120)
    print("="*52, " Contact Book ", "="*52)
    print("="*120)
    print("="*120)