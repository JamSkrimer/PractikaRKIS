import sqlite3

class Student:
    def __init__(self, name, surname, patronymic, group, marks):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.marks = marks

    def info_name(self):
        return self.name
    def info_surname(self):
        return self.surname
    def info_patronymic(self):
        return self.patronymic
    def info_group(self):
        return self.group
    def info_marks(self):
        return self.marks

class DataBas:
    def __init__(self, db_name="Univ.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student (
            name TEXT,
            surname TEXT,
            patronymic TEXT,
            "group" TEXT,
            marks TEXT
        )""")
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()

    def add_student(self, student):
        self.cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?)", (
            student.info_name(), student.info_surname(), student.info_patronymic(),
            student.info_group(), str(student.info_marks())))
        self.connection.commit()
        print("Студент был добавлен.")

    def view_all_students(self):
        self.cursor.execute("SELECT * FROM student")
        students = self.cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print("Список пуст")

    def check_average(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            name, surname, patronymic, group, marks_str = student_data
            marks = [int(i) for i in marks_str.strip("[]").split(", ")]
            average_grade = sum(marks) / len(marks)
            print("Информация о студенте:", name, surname, patronymic, "Группы: ", group)
            print("Его оценки: ", marks)
            print("Средний балл: ", average_grade)
        else:
            print("Студент с такой фамилией не найден.")

    def edit_student(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            name, surname, patronymic, group, marks = student_data
            new_name = input("Введите новое Имя студента: ")
            new_surname = input("Введите новую фамилию студента: ")
            new_patronymic = input("Введите новое отчество студента: ")
            new_group = input("Введите новую группу студента: ")
            new_marks = []
            for i in range(4):
                grade = int(input(f"Введите новую оценку {i + 1}: "))
                new_marks.append(grade)
            Student1 = Student(new_name, new_surname, new_patronymic, new_group, str(new_marks))
            self.cursor.execute("UPDATE student SET name = ? WHERE name = ?", (Student1.info_name(), name))
            self.cursor.execute("UPDATE student SET surname = ? WHERE surname = ?",
                                  (Student1.info_surname(), surname))
            self.cursor.execute("UPDATE student SET patronymic = ? WHERE patronymic = ?",
                                  (Student1.info_patronymic(), patronymic))
            self.cursor.execute("UPDATE student SET 'group' = ? WHERE 'group' = ?", (Student1.info_group(), group))
            self.cursor.execute("UPDATE student SET marks = ? WHERE marks = ?",
                                  (Student1.info_marks(), marks))
            self.connection.commit()
        else:
            print("Студент не найден.")

    def delete_student(self,surname):
        self.cursor.execute("SELECT * FROM student WHERE surname = ?", (surname,))
        student_data = self.cursor.fetchone()
        if student_data:
            self.cursor.execute("DELETE FROM student WHERE surname=?", (surname,))
        else:
            print("Студент не найден.")
        self.connection.commit()

    def view_group_average(self,group):
        self.cursor.execute("SELECT marks FROM student WHERE \"group\" = ?", (group,))
        marks_mas = self.cursor.fetchall()
        if marks_mas:
            counter = 0
            counter_student = 0
            for marks_tuple in marks_mas:
                marks_str = marks_tuple[0]
                marks = [int(i) for i in marks_str.strip("[]").split(", ")]
                grade = sum(marks) / len(marks)
                counter += grade
                counter_student += 1
            a = counter / counter_student
            print(f"Средний балл для группы = ", a)
        else:
            print("Группа не найдена")
db_manager = DataBas()

while True:
    print("1 - Добавить студента")
    print("2 - просмотр студентов")
    print("3 - просмотр студента")
    print("4 - изменить студента")
    print("5 - удалить студента")
    print("6 - ср. балл группы")
    print("0 - выход")

    choice = int(input())
    if choice == 1:
        name = input("Введите имя Студента: ")
        surname = input("Введите фамилию Студента: ")
        patronymic = input("Введите отчество Студента: ")
        group = input("Введите группу Студента: ")
        marks = []
        for i in range(4):
            grade = int(input(f"Введите оценку {i + 1}: "))
            marks.append(grade)
        Student1 = Student(name, surname, patronymic, group, marks)
        db_manager.add_student(Student1)
    elif choice == 2:
        db_manager.view_all_students()
    elif choice == 3:
        surname = input("Введите фамилию студента для поиска: ")
        db_manager.check_average(surname)
    elif choice == 4:
        surname = input("Введите фамилию студента для редакции: ")
        db_manager.edit_student(surname)
    elif choice == 5:
        surname = input("Введите фамилию студента для удаления)- ")
        db_manager.delete_student(surname)
    elif choice == 6:
        group = input("Введите группу студентов чтобы узнать ср.балл: ")
        db_manager.view_group_average(group)
    elif choice == 0:
        break

db_manager.close()