class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_current(self):
        return self.value


def print_menu():
    print("\nВыберите действие:")
    print("1. Показать текущее значение")
    print("2. Увеличить значение")
    print("3. Уменьшить значение")
    print("4. Выход")


counter = Counter()

while True:
    print_menu()
    choice = input("Ваш выбор: ")

    if choice == "1":
        print(f"Текущее значение: {counter.get_current()}")
    elif choice == "2":
        counter.increment()
        print("Значение увеличено")
    elif choice == "3":
        counter.decrement()
        print("Значение уменьшено")
    elif choice == "4":
        print("Программа завершена")
        break