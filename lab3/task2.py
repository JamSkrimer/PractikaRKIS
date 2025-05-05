class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def salary(self):
        return self.__rate * self.__days
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname

worker1 = Worker("Иван", "Втихоряевич", 2000, 31)

print(f"{worker1.get_name()} {worker1.get_surname()}")
print(f"Зарплата: {worker1.salary()} рублей.")
