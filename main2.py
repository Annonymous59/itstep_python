class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, hours):
        self.grade += hours * 0.1

    def play(self, hours):
        self.grade -= hours * 0.5

    def get_grade(self):
        return self.grade

student = Student("Tyler durden", 2)

lesson = float(input("Teach student: "))
student.study(lesson)

game = float(input("Play with student: "))
student.play(game)

grade = student.get_grade()

print(f"Student {student.name} Mark {student.grade}")