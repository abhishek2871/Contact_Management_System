class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class Contactmanagementsystem:
    def __init__(self):
        self.contacts = []

    # Add contact
    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    # View contacts
    def view(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"[{idx}]. {contact}")

    # Update Contact
    def update(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.name = name
            contact.phone = phone
            contact.email = email
            contact.address = address
            print("Contact updated successfully!")
        else:
            print("Invalid index!")

    # Delete contact
    def delete(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid index!")

    # Search Contact
    def search_contact(self, search_name):
        found_contacts = [contact for contact in self.contacts if search_name.lower() in contact.name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

    # Display Menu
    @staticmethod
    def display_menu():
        print("---------------------------------------------".center(130))
        print("--- Contact Management System ---".center(130))
        print("---------------------------------------------".center(130))
        print("1. Add Contact".center(128))
        print("2. View Contacts".center(128))
        print("3. Update Contact".center(128))
        print("4. Delete Contact".center(128))
        print("5. Search Contact".center(128))
        print("6. Exit".center(128))


def main():
    cms = Contactmanagementsystem()

    while True:
        Contactmanagementsystem.display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            cms.add_contact(name, phone, email, address)
        
        elif choice == '2':
            cms.view()

        elif choice == '3':
            cms.view()
            index = int(input("Enter the index of the contact to update: ")) - 1
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            cms.update(index, name, phone, email, address)

        elif choice == "4":
            cms.view()
            index = int(input("Enter the index of the contact to delete: ")) - 1
            cms.delete(index)
        
        elif choice == "5":
            search_name = input("Enter name to search: ")
            cms.search_contact(search_name)
        
        elif choice == "6":
            print("Exiting Contact Management System...")
            break
        
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
