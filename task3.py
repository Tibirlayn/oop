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
    
# лекторы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Среднее значение оценок лектора
    def average_grades(self):
        all_grades = []

        for grades_list in self.grades.values():
            all_grades.extend(grades_list)

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    # Оператор сравнения
    def __gt__(self, other):
        return self.average_grades() > other.average_grades()

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

some_lecturer = Lecturer('Иван', 'Иванов')
some_reviewer = Reviewer('Пётр', 'Петров')
some_student = Student('Алёхина', 'Ольга', 'Ж')
 
some_student.courses_in_progress += ['Python', 'Git']
some_lecturer.courses_attached += ['Python', 'C++', 'Git']
some_reviewer.courses_attached += ['Python', 'C++']

# выставление оценок лектору
some_student.rate_lecture(some_lecturer, 'Python', 7)   
some_student.rate_lecture(some_lecturer, 'Python', 8)
some_student.rate_lecture(some_lecturer, 'Git', 8)
some_student.rate_lecture(some_lecturer, 'Git', 9)
some_student.rate_lecture(some_lecturer, 'Java', 8)     
some_student.rate_lecture(some_lecturer, 'С++', 8)   

some_student.rate_lecture(some_reviewer, 'Python', 6)   

# выставление оценок студенту
some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 7)
some_reviewer.rate_hw(some_student, 'Git', 8)

# Завершенные курсы
some_reviewer.close_course(some_student, 'Введение в программирование')

print(some_reviewer)
print(some_lecturer)
print(some_student)

# Задача 2. Оператор сравнения
print("Слабая подготовка студента при сильном преподавании" if some_lecturer > some_student else "Сильная подготовка студента при слабом преподавании")
