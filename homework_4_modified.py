class Number:
    def __init__(self, value):
        self.__value = value
   
    def __eq__(self, other):
        return self.__value == other.__value

    def __lt__(self, other):
        return self.__value < other.__value

    def __gt__(self, other):
        return self.__value > other.__value


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
            grade1_my_num = Number (grade1)
            grade2_my_num = Number (grade2)
            if grade1_my_num == grade2_my_num:
                return "У лекторов одинаковая средняя оценка"
            elif grade1_my_num > grade2_my_num:
                return f"У лектора: {self.name} средняя оценка выше, чем у лектора: {other.name}"
            else:
                return f"У лектора: {other.name} средняя оценка выше, чем у лектора: {self.name}"
        elif isinstance(self, Student) and isinstance(other, Student):
            grade1 = CommonStLect.avg (self)
            grade2 = CommonStLect.avg (other)
            grade1_my_num = Number (grade1)
            grade2_my_num = Number (grade2)
            if grade1_my_num == grade2_my_num:
                return "У студентов одинаковая средняя оценка"
            elif grade1_my_num > grade2_my_num:
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

def avg_student_grade_in_course(student_list, course):
    sum_grade_course = 0
    grade_count_course = 0

    for st in student_list:
        if isinstance(st, Student):
            if course in st.grades:
                sum_grade_course = sum_grade_course + sum(st.grades [course])
                grade_count_course = len(st.grades [course]) + grade_count_course

    if grade_count_course == 0:
        return 0.0
    else:
        return round (sum_grade_course/grade_count_course,1)

def lector_grade_in_course(lector_list, course):
    sum_grade_course = 0
    grade_count_course = 0

    for st in lector_list:
        if isinstance(st, Lecturer):
            if course in st.grades:
                sum_grade_course = sum_grade_course + sum(st.grades [course])
                grade_count_course = len(st.grades [course]) + grade_count_course

    if grade_count_course == 0:
        return 0.0
    else:
        return round (sum_grade_course/grade_count_course,1)

student_1 = Student('Ruoy_1', 'Eman_1', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['C++']

student_2 = Student('Ruoy_2', 'Eman_2', 'your_gender')
student_2.courses_in_progress += ['Java']
student_2.courses_in_progress += ['C++']

lector_1 = Lecturer('Some_1', 'Buddy_1')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['C++']

lector_2 = Lecturer('Some_2', 'Buddy_2')
lector_2.courses_attached += ['Java']
lector_2.courses_attached += ['C++']

student_1.rate_lect(lector_1, 'C++', 10)
student_1.rate_lect(lector_1, 'Python', 10)
student_1.rate_lect(lector_2, 'C++', 9)
student_2.rate_lect(lector_1, 'C++', 10)
student_2.rate_lect(lector_2, 'Java', 10)
student_2.rate_lect(lector_2, 'C++', 7)

print(lector_1)
print(lector_2)

reviewer1 = Reviewer('Rev', 'iewer')
reviewer1.courses_attached += ['Java','Python','C++']
reviewer1.rate_hw(student_1, 'Python', 10)
reviewer1.rate_hw(student_1, 'C++', 10)
reviewer1.rate_hw(student_1, 'C++', 9)
reviewer1.rate_hw(student_1, 'C++', 10)
reviewer1.rate_hw(student_1, 'Python', 10)
reviewer1.rate_hw(student_1, 'Python', 10)
reviewer1.rate_hw(student_2, 'Java', 7)
reviewer1.rate_hw(student_2, 'C++', 10)
reviewer1.rate_hw(student_2, 'C++', 6)

print(student_1)
print(student_2)
print(student_1.compare(student_2))
print(lector_1.compare(lector_2))

students_list = [student_1,student_2]
lectors_list = [lector_1,lector_2]
print(avg_student_grade_in_course (students_list,"C++"))
print(lector_grade_in_course (lectors_list,"C++"))


