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

    def avg_rate(self):
        grades_list = sum(self.grades.values(), [])
        print(grades_list)
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

    def avg_rate(self):
        grades_list = sum(self.grades.values(), [])
        print(grades_list)
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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

cool_lector = Lecturer('Some', 'Buddy')
cool_lector.courses_attached += ['Python', 'Java']

best_student.rate_lecturer(cool_lector, 'Python', 10)
best_student.rate_lecturer(cool_lector, 'Python', 8)
best_student.rate_lecturer(cool_lector, 'Java', 5)

print(cool_reviewer)
print(cool_lector)
print(best_student)
