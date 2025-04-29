class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades

    def get_info(self):
        return f"Фамилия: {self.surname}\nДата рождения: {self.birth_date}\nНомер группы: {self.group_number}\nОценки: {self.grades}"
def show_students(students):
    for i, student in enumerate(students, 1):
        print(f"\nСтудент #{i}\n{student.get_info()}")

def main():
    students = [
        Student("Иванов", "01.01.2000", "101", [4, 5, 4, 5, 5]),
        Student("Петров", "15.03.2001", "102", [5, 5, 5, 5, 5]),
        Student("Сидоров", "20.06.2000", "101", [3, 4, 4, 4, 5])
    ]
    while True:
        print("\n1. Показать студентов\n2. Найти студента\n3. Изменить данные\n4. Выход")
        menu = input("Выберите действие (1-4): ")

        if menu == "1":
            show_students(students)
        elif menu == "2":
            surname = input("Фамилия: ")
            birth_date = input("Дата рождения: ")
            found = next((s for s in students if s.surname == surname and s.birth_date == birth_date), None)
            print(found.get_info() if found else "Студент не найден")
        elif menu == "3":
            show_students(students)
            try:
                id = int(input("Номер студента: ")) - 1
                if 0 <= id < len(students):
                    student = students[id]
                    field = input("Что изменить (фамилия/дата/группа): ").lower()
                    value = input("Новое значение: ")
                    if field == "фамилия": student.surname = value
                    elif field == "дата": student.birth_date = value
                    elif field == "группа": student.group_number = value
                    print("Обновлено:", student.get_info())
            except ValueError:
                print("Ошибка ввода")
        elif menu == "4":
            break
if __name__ == "__main__":
    main()
