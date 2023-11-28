class CommonStLect:

    def avg (self):
        if isinstance(self, Student) or isinstance(self, Lecturer):
            grade_sum = 0
            grade_count = 0
            for grades in self.grades.values():
                grade_count = len(grades) + grade_count
                grade_sum = grade_sum + sum(grades)
            if grade_count == 0:
                return 0.0
            else:
                return round (grade_sum/grade_count,1)
        else:
            return 'Ошибка'
   
    def compare (self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            grade1 = CommonStLect.avg (self)
            grade2 = CommonStLect.avg (other)
            if grade1 == grade2:
                return "У лекторов одинаковая средняя оценка"
            elif grade1 > grade2:
                return f"У лектора: {self.name} средняя оценка выше, чем у лектора: {other.name}"
            else:
                return f"У лектора: {other.name} средняя оценка выше, чем у лектора: {self.name}"
        elif isinstance(self, Student) and isinstance(other, Student):
            grade1 = CommonStLect.avg (self)
            grade2 = CommonStLect.avg (other)
            if grade1 == grade2:
                return "У студентов одинаковая средняя оценка"
            elif grade1 > grade2:
                return f"У студента: {self.name} средняя оценка выше, чем у студента: {other.name}"
            else:
                return f"У студента: {other.name} средняя оценка выше, чем у студента: {self.name}"
        else:
            return 'Ошибка' 
  

class Student (CommonStLect):

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grade = CommonStLect.avg (self)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor,CommonStLect):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
   
    def __str__(self):
        grade = CommonStLect.avg (self)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {grade}"


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.courses_in_progress += ['Python']
cool_student.courses_in_progress += ['C++']
best_lector = Lecturer('Some', 'Buddy')
best_lector.courses_attached += ['Python']
best_lector.courses_attached += ['C++']
cool_student.rate_lect(best_lector, 'C++', 10)
cool_student.rate_lect(best_lector, 'Python', 10)
cool_student.rate_lect(best_lector, 'Python', 10)
print(best_lector)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Java']
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)
print(best_student)


# для задания 2
best_lector2 = Lecturer('Some2', 'Buddy2')
best_lector2.courses_attached += ['Python']
best_lector2.courses_attached += ['C++']
cool_student.rate_lect(best_lector2, 'C++', 3)
cool_student.rate_lect(best_lector2, 'Python', 4)
cool_student.rate_lect(best_lector2, 'Python', 5)

best_student2 = Student('Ruoy2', 'Eman2', 'your_gender2')
best_student2.courses_in_progress += ['Java']
cool_reviewer.rate_hw(best_student2, 'Java', 10)
cool_reviewer.rate_hw(best_student2, 'Java', 9)
cool_reviewer.rate_hw(best_student2, 'Java', 10)

print(best_student.compare(best_student2))

