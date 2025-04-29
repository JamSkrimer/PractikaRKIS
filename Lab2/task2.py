class Train:
    def __init__(self, destination, number, time):
        self.destination = destination
        self.number = number
        self.time = time
    def get_info(self):
        return f"Пункт назначения: {self.destination}\nНомер поезда: {self.number}\nВремя отправления: {self.time}"
def main():
    trains = [
        Train("Саратов", "666", "06:00"),
        Train("Санкт-Петербург", "052", "10:30"),
        Train("Алжир", "100", "12:15")
    ]
    while True:
        print("1. Показать все поезда")
        print("2. Найти поезд по номеру")
        print("3. Выход")
        menu = input("Выберите действие (1-3): ")
        if menu == "1":
            print("\nСписок всех поездов:")
            for train in trains:
                print(f"{train.get_info()}\n")

        elif menu == "2":
            number = input("Введите номер поезда: ")
            found = False
            for train in trains:
                if train.number == number:
                    print("\nНайденный поезд:")
                    print(train.get_info())
                    found = True
                    print("\n")
                    break
            if not found:
                print("Поезд не найден")
        elif menu == "3":
            break
if __name__ == "__main__":
    main()
