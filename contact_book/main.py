import json

def get_all_contacts():
  with open("contacts.json") as json_file:
    return json.load(json_file)

def get_all_name():
  contacts = get_all_contacts()
  
  contact_name = []
  for i in range(len(contacts)):
    contact_name.append(contacts[i]["name"])

  return contact_name

def search(contact_name, contact_input):
    for i in range(len(contact_name)):
      if contact_name[i] == contact_input:
        return True
    return False

def show_contacts():
  contacts = get_all_contacts()
  
  print("\n>>> Contact list <<<")
  for i in range(len(contacts)):
    print(
      f"{i+1}"+ ". " + contacts[i]["name"] + " - " +   
      contacts[i]["number"] + " - " + contacts[i]
      ["email"])

  print("\n")

def add_contact():
  contacts = get_all_contacts()

  nama = input("Name: ").strip().title()
  number = input("Phone Number: ")
  email = input("Email: ").strip()

  contacts.append({
    "name": nama,
    "number": number,
    "email": email
  })

  with open("contacts.json", "w") as json_file:
    json.dump(contacts, json_file)

    print(">>> Contact successfully saved <<<\n")

def edit_contact():
  contacts = get_all_contacts()
  contacts_name = get_all_name()
  
  contact_input = input("Input contact name: ").strip().title()

  if search(contacts_name, contact_input):
    new_name = input("Input new name: ").strip().title()
    new_number = input("Phone Number: ")
    new_email = input("Email: ").strip()
    index = contacts_name.index(contact_input)

    for i in range(len(contacts_name)):
      if i == index:
        if new_name != "":
          contacts[i]["name"] = new_name
        if new_number != "":
          contacts[i]["number"] = new_number
        if new_email != "":
          contacts[i]["email"] = new_email
    
    print(">>> Contact successfully updated <<<\n")
  else:
    print("Contact not found")

  with open("contacts.json", "w") as json_file:
    json.dump(contacts, json_file)
      
def delete_contact():
  contacts = get_all_contacts()
  contacts_name = get_all_name()
  
  contact_input = input("Input contact name: ").strip().title()

  if search(contacts_name, contact_input):
    index = contacts_name.index(contact_input)
    for i in range(len(contacts_name)):
      if i == index:
        del(contacts[i])
    print(">>> Contact successfully deleted <<<\n")
  else:
      print("Contact not found")
      
  with open("contacts.json", "w") as json_file:
    json.dump(contacts, json_file)
    
menu_prompt = """>>> Please enter one of the following options <<<

- 'l' to list the contacts
- 'a' to add a contact
- 'e' to edit a contact
- 'd' to delete a contact
- 'q' to quit

What would you like to do? """
selected_option = input(menu_prompt).strip().lower()

while selected_option != "q":
  if selected_option == "l":
    show_contacts()
  elif selected_option == "a":
    add_contact()
  elif selected_option == "e":
    edit_contact()
  elif selected_option == "d":
    delete_contact()
  else:
    print(f"Sorry, '{selected_option}' isn't a valid option.")
    
  selected_option = input(menu_prompt).strip().lower()