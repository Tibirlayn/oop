class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # метод выставление оценок лектору
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    # Среднее значение оценок студента
    def average_grades(self):
        all_grades = []

        for grades_list in self.grades.values():
            all_grades.extend(grades_list)

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)
    
    # Среднее значение оценок студентов
    def ave_grades(students, course):
        all_grades = []

        for student in students:
            if course in student.grades:
                all_grades.extend(student.grades[course])

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)
    
    
    def __str__(self):
        grades = self.average_grades()
        courses = ", ".join(self.courses_in_progress)
        finished = ", ".join(self.finished_courses)
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {grades}
Курсы в процессе изучения: {courses}
Завершенные курсы: {finished} \n"""
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""
    
# лекторы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        all_grades = []

        for grades_list in self.grades.values():
            all_grades.extend(grades_list)

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    # Среднее значение оценок лекторов
    def ave_grades(lecturers, cource):
        all_grades = []

        for lecturer in lecturers:
            if cource in lecturer.grades:
                all_grades.extend(lecturer.grades[cource])

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

     # Оператор сравнения
    def __gt__(self, other):
        return self.average_grades() > other.average_grades()
    
    def __eq__(self, other):
        return self.average_grades() == other.average_grades()

    def __lt__(self, other):
        return self.average_grades() < other.average_grades()
    
    def __rgt__(self, other):
        return self.average_grades() > other.average_grades()
    
    def __req__(self, other):
        return self.average_grades() == other.average_grades()

    def __rlt__(self, other):
        return self.average_grades() < other.average_grades()

    def __str__(self):
        grades = self.average_grades()
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {grades}"""

# эксперты, проверяющие домашние задания
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # метод выставление оценок студенту
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    # метод Завершенные курсы
    def close_course(self, student, topic):
        if isinstance(student, Student):
            student.finished_courses.append(topic)
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""
    
# Лекторы
ivanov_lecturer = Lecturer('Иван', 'Иванов')
smith_lecturer = Lecturer('Джон', 'Смит')
sidorov_lecturer = Lecturer('Алексей', 'Сидоров')

# Проверяющие (Ревьюеры)
petrov_reviewer = Reviewer('Пётр', 'Петров')
black_reviewer = Reviewer('Блэк', 'Джек')
volkov_reviewer = Reviewer('Владимир', 'Волков')

# Студенты
alyokhina_student = Student('Ольга', 'Алёхина', 'Ж')
ivanova_student = Student('Мария', 'Иванова', 'Ж')
petrov_student = Student('Кирилл', 'Петров', 'М')

# Лекторы ведут свои предметы
ivanov_lecturer.courses_attached += ['Python']
smith_lecturer.courses_attached += ['Git']
sidorov_lecturer.courses_attached += ['Python', 'Git']

# Ревьюеры проверяют свои предметы
petrov_reviewer.courses_attached += ['Python']
black_reviewer.courses_attached += ['Git']
volkov_reviewer.courses_attached += ['Python', 'Git']

# студенты изучают 
alyokhina_student.courses_in_progress += ['Python', 'Git']
ivanova_student.courses_in_progress += ['Python', 'Git']
petrov_student.courses_in_progress += ['Python', 'Git']

# Ревьюеры ставят оценки студентам)
petrov_reviewer.rate_hw(alyokhina_student, 'Python', 10)
black_reviewer.rate_hw(ivanova_student, 'Git', 9)
volkov_reviewer.rate_hw(petrov_student, 'Python', 8)
volkov_reviewer.rate_hw(petrov_student, 'Git', 7)

# Студенты ставят оценки лекторам
alyokhina_student.rate_lecture(ivanov_lecturer, 'Python', 10)
ivanova_student.rate_lecture(smith_lecturer, 'Git', 8)
petrov_student.rate_lecture(sidorov_lecturer, 'Python', 9)

# Завершенные курсы
petrov_reviewer.close_course(alyokhina_student, 'Введение в программирование')

student_list = [alyokhina_student, ivanova_student, petrov_student]
lecturer_list = [ivanov_lecturer, smith_lecturer, sidorov_lecturer]

print(ivanov_lecturer) 
print(petrov_reviewer)
print(alyokhina_student)

# Задача 3. Пункт 2: Оператор сравнения
print(ivanov_lecturer < petrov_student)
print()

# Задание 4
result_student = Student.ave_grades(student_list, 'Python') # подсчета средней оценки за домашние задания
result_lecturer = Lecturer.ave_grades(lecturer_list, 'Git') # подсчета средней оценки за лекции

print(f"Средняя оценка за лекции Git: {result_lecturer}") 
print(f"Средняя оценка за домашние задания Python: {result_student}")