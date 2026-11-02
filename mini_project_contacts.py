# Contact
print("\n****** Contact number ******")
print("1. add_contact")
print("2. search_contact")
print("3. update_contact")
print("4. delete_contact")
print("5. view_contact")
print("6. Exit")

contacts={}

def add_contacts():
    name = input("Enter name:")
    phone = input("Enter phone number :")
    contacts[name] = phone
    print("Contact added successfully!")

def search_contacts():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Phone number:", contacts[name])
    else:
        print("Contact not found!")

def update_contacts():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def  delete_contacts():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def view_contacts():
     if contacts:
            for name, phone in contacts.items():
               print(name, ":", phone)
            else:
                print("No contacts available!")

choice = input("Enter your choice: ")
if choice == "1":
    add_contacts()
elif choice == "2":
    search_contacts()
elif choice == "3":
    update_contacts()
elif choice == "4":
    delete_contacts()
elif choice == "5":
    view_contacts()
elif choice == "6":
    print("Thank you!")
else:
    print("Invalid choice!")