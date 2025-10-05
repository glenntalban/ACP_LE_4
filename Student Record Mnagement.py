import os

doc_path = os.path.expanduser("~/Documents")
if not os.path.exists(doc_path):
    os.makedirs(doc_path)

def register_student():
    print("\n----Register Student----")
    student_no = input("Sudent No.: ")
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    middle_initial = input("Middle Initial: ")
    program = input("Program: ")
    age = input("Age: ")
    gender = input("Gender: ")
    birhtday = input("Birthday: ")
    contact_no = input("Contact No: ")

    data = [
        f"Student No.: {student_no}",
        f"Full Name: {first_name} {middle_initial} {last_name}",
        f"Program: {program}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Birthday: {birhtday}",
        f"Contact No.: {contact_no}"
    ]

    
    file_name = f"{student_no}.txt"
    file_path = os.path.join(doc_path, file_name)

    try:
        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")
        print(f"Student record saved to {file_path}")
    except Exception as e:
        print(f"Error saving student record: {e}")

def open_student_record():

    print("\n----Open Student Record----")
    student_no = input("Enter Student No.: ")
    print("\n---Student Record---")
    file_name = f"{student_no}.txt"
    file_path = os.path.join(doc_path, file_name)

    try:
        with open(file_path, "r") as f:
            for line in f:
                print(line.strip())
        print("\n--------------------\n")
    except FileNotFoundError:
        print("Student record not found.")
    except Exception as e:
        print(f"Error opening student record: {e}")

while True:
    print("\nMenu:")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        open_student_record()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
