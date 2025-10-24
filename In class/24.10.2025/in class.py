class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = {}

    def attend_class(self, course_name, status=True):
        self.attendance[course_name] = status

    def get_attendance(self):
        return self.attendance


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def mark_attendance(self, student, course_name, status=True):
        if student in self.students:
            student.attend_class(course_name, status)
            print(f" {student.name} marked {'present' if status else 'absent'} for {course_name}.")
        else:
            print(f" {student.name} is not in {self.name}'s class!")

    def show_class_list(self):
        print(f"\n {self.name}'s {self.subject} Class Students:")
        for s in self.students:
            print(f"- {s.name} ({s.student_id})")



teacher = Teacher("Kipral", "ICT")

s1 = Student("Loc", "ST101")
s2 = Student("Daniel", "ST102")

teacher.add_student(s1)
teacher.add_student(s2)
teacher.show_class_list()

teacher.mark_attendance(s1, "ICT", True)
teacher.mark_attendance(s2, "ICT", True)

print("\n Attendance Records:")
for s in teacher.students:
    print(f"{s.name}: {s.get_attendance()}")
