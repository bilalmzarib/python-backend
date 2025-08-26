import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
)
""")


def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("✔️ Student added successfully.")


def list_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if not students:
        print("⚠️ No students found.")
    else:
        print("\n📋 Student List:")
        for student in students:
            print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Grade: {student[3]}")

def update_student(student_id, name, age, grade):
    cursor.execute("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?", (name, age, grade, student_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("⚠️ No student found with that ID.")
    else:
        print("🛠️ Student updated successfully.")


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print(" No student found with that ID.")
    else:
        print(" Student deleted successfully.")


def menu():
    while True:
        print("\n=== Student Database Manager ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print(" Invalid age. Please enter a number.")
                continue
            grade = input("Enter student grade: ")
            add_student(name, age, grade)

        elif choice == "2":
            list_students()

        elif choice == "3":
            try:
                student_id = int(input("Enter student ID to update: "))
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                grade = input("Enter new grade: ")
                update_student(student_id, name, age, grade)
            except ValueError:
                print(" Invalid input. Make sure IDs and ages are numbers.")

        elif choice == "4":
            try:
                student_id = int(input("Enter student ID to delete: "))
                delete_student(student_id)
            except ValueError:
                print(" Invalid input. ID must be a number.")

        elif choice == "5":
            print("👋 Exiting the program. Goodbye!")
            break

        else:
            print(" Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    menu()
    conn.close()
