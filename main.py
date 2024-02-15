class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {self.avg_rate()} \n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __gt__(self, student):
        if isinstance(student, Student):
            return self.avg_rate() > student.avg_rate()
        else:
            return f"{student.name} не является объектом класса Student"

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.avg_rate() < student.avg_rate()
        else:
            return f"{student.name} не является объектом класса Student"

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.avg_rate() == student.avg_rate()
        else:
            return f"{student.name} не является объектом класса Student"

    def avg_rate(self):
        grades_list = sum(self.grades.values(), [])
        return sum(grades_list) / len(grades_list)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_rate()}"

    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_rate() > lecturer.avg_rate()
        else:
            return f"{lecturer.name} не является объектом класса Lecturer"

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_rate() < lecturer.avg_rate()
        else:
            return f"{lecturer.name} не является объектом класса Lecturer"

    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avg_rate() == lecturer.avg_rate()
        else:
            return f"{lecturer.name} не является объектом класса Lecturer"

    def avg_rate(self):
        grades_list = sum(self.grades.values(), [])
        return sum(grades_list) / len(grades_list)


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_ivanov_a = Student('Алексей', 'Иванов', 'Мужской')
student_ivanov_a.courses_in_progress += ['Python', 'Java']
student_sokolov_k = Student('Кирилл', 'Соколов', 'Мужской')
student_sokolov_k.courses_in_progress += ['Python']

reviewer_morozov_p = Reviewer('Павел', 'Морозов')
reviewer_morozov_p.courses_attached += ['Python']
reviewer_stepanov_v = Reviewer('Вадим', 'Степанов')
reviewer_stepanov_v.courses_attached += ['Python', 'Java']

reviewer_morozov_p.rate_hw(student_sokolov_k, 'Python', 10)
reviewer_stepanov_v.rate_hw(student_sokolov_k, 'Python', 7)
reviewer_stepanov_v.rate_hw(student_ivanov_a, 'Java', 9)
reviewer_stepanov_v.rate_hw(student_ivanov_a, 'Python', 9)

lector_morozov_p = Lecturer('Павел', 'Морозов')
lector_morozov_p.courses_attached += ['Python']
lector_popov_d = Lecturer('Данил', 'Попов')
lector_popov_d.courses_attached += ['Python', 'Java']

student_ivanov_a.rate_lecturer(lector_morozov_p, 'Python', 8)
student_ivanov_a.rate_lecturer(lector_popov_d, 'Java', 10)
student_ivanov_a.rate_lecturer(lector_popov_d, 'Python', 9)

print(student_sokolov_k)
print()

print(reviewer_stepanov_v)
print()

print(lector_morozov_p)
print()

print(lector_morozov_p == lector_popov_d)
print(lector_morozov_p < lector_popov_d)
print(lector_morozov_p > lector_popov_d)
print()

print(student_sokolov_k == student_ivanov_a)
print(student_sokolov_k < student_ivanov_a)
print(student_sokolov_k > student_ivanov_a)
