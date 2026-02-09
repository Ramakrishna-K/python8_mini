class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks


    def to_string(self):
        return f"{self.name},{self.roll},{self.marks}\n" 
       

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    s = Student(name, roll, marks)

    with open("student.txt","a") as f:
        f.write(s.to_string())
    print("student add successfully")    


def display_students():
    try:
        with open("student.txt","r") as f:
            for line in f:
                name , roll, marks = line.strip().split(",")
                print(f"Name: {name}, Roll: {roll}, Marks: {marks}")

    except FileNotFoundError:
        print("No student records founds")            

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")



