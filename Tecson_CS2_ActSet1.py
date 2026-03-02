def main():
    student = {}

    print("--- Student Information Collector ---")
    
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    subject = input("Enter favorite subject: ")

    student["name"] = name
    student["age"] = age
    student["subject"] = subject

    print("\n--- Student Details ---")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Favorite Subject: {student['subject']}")

if __name__ == "__main__":
    main()