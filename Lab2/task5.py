class SimpleClass:
    def __init__(self, x=10, y=20):
        self.x = x
        self.y = y
        print(f"Создан объект со значениями: x={x} и y={y}")

    def __del__(self):
        print(f"Удален объект со значениями: x={self.x} и y={self.y}")

def print_menu():
    print("\nВыберите действие:")
    print("1. Создать объект с заданными значениями")
    print("2. Создать объект со значениями по умолчанию")
    print("3. Показать текущие значения объекта")
    print("4. Удалить текущий объект")
    print("5. Выход")
obj = None

while True:
    print_menu()
    choice = input("Ваш выбор: ")
    if choice == "1":
        x = int(input("Введите значение x: "))
        y = int(input("Введите значение y: "))
        obj = SimpleClass(x, y)
    elif choice == "2":
        obj = SimpleClass()
    elif choice == "3":
        if obj:
            print(f"Текущие значения: x={obj.x}, y={obj.y}")
        else:
            print("Объект еще не создан")
    elif choice == "4":
        if obj:
            del obj
            obj = None
        else:
            print("Объект еще не создан")
    elif choice == "5":
        break
