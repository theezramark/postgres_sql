students = {"name":"Steven", "grades":(89, 23, 45, 98)}

def avg(sequence):
    return sum(sequence) / len(sequence)

print(avg(students["grades"]))

class student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades[0]

    def avg(self):
        print(self.grades)
        return sum(self.grades) / len(self.grades)

student_one = student("Carl", (89, 23, 45, 98))
print(student_one.avg())