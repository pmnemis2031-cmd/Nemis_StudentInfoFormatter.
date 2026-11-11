first_name = input("Enter first name: ").strip
last_name = input("Enter last name: ").strip
section = input("Enter section: ").strip
favorite_subject = input("Enter favorite subject: ").strip

#Combine name
full_name = f"{first_name} {last_name}"

print("\nFormatted Output: ")
print("Name: ", full_name.title())
print("Name Code: ",full_name.upper())
print("Section: ",section.upper())
print("Fvorite Subject: ",favorite_subject.title())
print("Character Count: ",len(full_name))
