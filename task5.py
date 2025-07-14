contacts = []

def add_contact():
    print("\n➕ Add New Contact")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.")
        return
    print("\n📇 Contact List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    print("\n🔍 Search Contact")
    keyword = input("Enter name or phone number to search: ")
    found = False
    for c in contacts:
        if keyword.lower() in c['name'].lower() or keyword in c['phone']:
            print("\n✅ Contact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def update_contact():
    print("\n✏️ Update Contact")
    name = input("Enter the name of the contact to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("New Phone Number: ")
            c['email'] = input("New Email: ")
            c['address'] = input("New Address: ")
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    print("\n🗑️ Delete Contact")
    name = input("Enter the name of the contact to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("✅ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

def main():
    while True:
        print("\n===== 📖 Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")

# Run the program
main()
