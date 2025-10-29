class Student:
    def __init__(self, name, age, roll_number=None):
        self.roll_number=roll_number
        self.name = name
        self.age = age
        self.subjects = {}
        self.grade = None

    def add_subject(self, subject, mark):
        self.subjects[subject] = mark

    def get_average(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90: self.grade = 'A+'
        elif avg >= 80: self.grade = 'A'
        elif avg >= 70: self.grade = 'B'
        elif avg >= 50: self.grade = 'C'
        elif avg < 34: self.grade = 'Fail'
        else: self.grade = 'D'
        return self.grade

    def get_report(self):
        self.get_grade()
        return f"{self.name} ({self.age} yrs)\nSubjects: {self.subjects}\nAverage: {self.get_average():.2f}\nGrade: {self.grade}"


class School:
    def __init__(self, name):
        self.next_roll=1
        self.name = name
        self.students = []

    def add_student(self, student):
        student.roll_number = self.next_roll
        self.students.append(student)
        print(f"✅ {student.name} added to {self.name} with roll number: {self.next_roll}")
        self.next_roll+=1

    def show_all_students(self):
        print(f"\n🎓 Students in {self.name}:")
        if not self.students:
            print("No students yet.")
            return
        for s in self.students:
            print(f"- {s.name} (Age: {s.age}, Roll Number: {s.roll_number}, Grade: {s.get_grade()})")

    def find_student(self, name, roll_number):
        for s in self.students:
            if s.name.lower() == name.lower() or int(roll_number)==s.roll_number:
                return s
        return None

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name.lower() != name.lower()]
        print(f"❌ {name} removed from {self.name}")


# 🧭 Menu-driven interface
def main():
    school = School("Sunshine High School")

    while True:
        print("\n===== School Menu =====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Find Student")
        print("4. Remove Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            student = Student(name, age)

            while True:
                subject = input("Enter subject name (or 'done' to stop): ")
                if subject.lower() == "done":
                    break
                mark = int(input(f"Enter marks for {subject}: "))
                student.add_subject(subject, mark)

            school.add_student(student)
            

        elif choice == "2":
            school.show_all_students()

        elif choice == "3":
            name = input("Enter student name to search: ")
            roll=input('Or enter roll number: ')
            s = school.find_student(name, roll_number=roll)
            if s:
                print("\n📘 Student Report:\n" + s.get_report())
            else:
                print("❌ Student not found!")

        elif choice == "4":
            name = input("Enter student name to remove: ")
            school.remove_student(name)

        elif choice == "5":
            print("👋 Exiting program... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
