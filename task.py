#Q1
items=['sqp','123','python']
result=list(filter(lambda x:x.isalpha(),items))
print(result)


#Q2
products = [
{'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
{'id': 3, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':True},
{'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':False}
]
in_stoks=list(filter(lambda p:p['instock']==True,products))
for i in in_stoks:
    print(i)


#Q3
course = [
    {'title': 'Ancient Civilizations','genre': 'history'},
    {'title': 'CorporateFinance', 'genre': 'commerce'},
    {'title': 'Modern World History', 'genre': 'history'}
    ]
history_genre=list(filter(lambda h:h['genre']=='history',course))
for i in history_genre:
    print(i)


#Q4
emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net','shyam.kumar@workcorp.com']
blacklist = ('@hooya.com', '@malware.net')
spam_emails = list(filter(lambda x:x.endswith(blacklist), emails))
print("Spam emails:", spam_emails)


# #Q5
price = [100, 50, 200, 75]
discounted_prices = list(map(lambda x: x * 0.8, price))
print("Discounted prices:", discounted_prices)


# #Q6
def skip_two(lst):
    return lst[1:12:3]
example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = skip_two(example_list)
print("Result:", result)


#Q7
def remove_at_idx(lst, index):
    if index < 0 or index >= len(lst):
        print("Error: Index out of range.")
        return lst
    return lst[:index] + lst[index+1:]

#Q8
import re
user_input = input("Enter your message: ")
cleaned_input = re.sub(r'[^a-zA-Z0-9]', '#', user_input)
print("Cleaned message:", cleaned_input)

#Q9
users_db = {}
def register_user(username, password, email):
    if username in users_db:
        return "Username already exists"
    users_db[username] = {'password': password, 'email': email}
    return f"Registration successful for {username}"
def login_user(username, password):
    if username not in users_db:
        return "User not found"
    if users_db[username]['password'] != password:
        return "Incorrect password"
    return f"Welcome back, {username}"
print(register_user('ram', 'ram123', 'ram@email.com'))
print(register_user('shyam', 'shyam456', 'shyam@email.com'))
print(register_user('hari', 'hari231', 'hari@email.com'))
print(login_user('ram', 'ram123'))
print(login_user('shyam', 'wrongpass'))
print(login_user('unknown', 'abc123'))

#Q10
inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]
def add_product():
    name = input("Enter product name: ").strip()
    # Prevent duplicate product names
    for product in inventory:
        if product['name'].lower() == name.lower():
            print("Product already exists!")
            return
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive numbers.")
            return
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be an integer.")
        return
    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print(f"Product '{name}' added successfully!")

def view_products():
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"{'Name':<15}{'Price':<10}{'Quantity':<10}")
    print("-"*35)
    for product in inventory:
        print(f"{product['name']:<15}{product['price']:<10}{product['quantity']:<10}")

def update_product():
    name = input("Enter product name to update: ").strip()
    for product in inventory:
        if product['name'].lower() == name.lower():
            try:
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))
                if price <= 0 or quantity <= 0:
                    print("Price and quantity must be positive numbers.")
                    return
            except ValueError:
                print("Invalid input. Price must be a number and quantity must be an integer.")
                return
            product['price'] = price
            product['quantity'] = quantity
            print(f"Product '{name}' updated successfully!")
            return
    print("Product not found.")

def delete_product():
    name = input("Enter product name to delete: ").strip()
    for product in inventory:
        if product['name'].lower() == name.lower():
            inventory.remove(product)
            print(f"Product '{name}' deleted successfully!")
            return
    print("Product not found.")

def total_inventory_value():
    total = sum(product['price'] * product['quantity'] for product in inventory)
    print(f"Total inventory value: {total}")
while True:
    print("\n=== Product Inventory Menu ===")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Update Product Details")
    print("4. Delete Product")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ").strip()
    if choice == '1':
        add_product()
    elif choice == '2':
        view_products()
    elif choice == '3':
        update_product()
    elif choice == '4':
        delete_product()
    elif choice == '5':
        total_inventory_value()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


#Q11
import re
contacts = [{'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}]
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
    return "@" in email and "." in email

def add_contact():
    name = input("Enter contact name: ").strip()
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Contact with this name already exists!")
            return
    
    phone = input("Enter phone number (10 digits): ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number! Must be 10 digits.")
        return
    
    email = input("Enter email address: ").strip()
    if not is_valid_email(email):
        print("Invalid email address! Must contain '@' and '.'")
        return
    
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print(f"Contact '{name}' added successfully!")

def display_contacts():
    if not contacts:
        print("No contacts to display.")
        return
    print(f"{'Name':<20}{'Phone':<15}{'Email':<25}")
    print("-"*60)
    for contact in contacts:
        print(f"{contact['name']:<20}{contact['phone']:<15}{contact['email']:<25}")

def search_contact():
    name = input("Enter name to search: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Contact found:")
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_phone = input("Enter new phone (leave blank to keep current): ").strip()
            new_email = input("Enter new email (leave blank to keep current): ").strip()
            
            if new_name:
                for c in contacts:
                    if c['name'].lower() == new_name.lower() and c != contact:
                        print("Another contact with this name already exists!")
                        return
                contact['name'] = new_name
            if new_phone:
                if not is_valid_phone(new_phone):
                    print("Invalid phone number! Must be 10 digits.")
                    return
                contact['phone'] = new_phone
            if new_email:
                if not is_valid_email(new_email):
                    print("Invalid email address! Must contain '@' and '.'")
                    return
                contact['email'] = new_email
            
            print(f"Contact '{name}' updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name of contact to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!")
            return
    print("Contact not found.")

def sort_contacts():
    contacts.sort(key=lambda x: x['name'].lower())
    print("Contacts sorted alphabetically by name.")
while True:
    print("\n=== Contact Management Menu ===")
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact by Name")
    print("4. Update Contact Information")
    print("5. Delete Contact")
    print("6. Sort Contacts Alphabetically")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        sort_contacts()
    elif choice == '7':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")


