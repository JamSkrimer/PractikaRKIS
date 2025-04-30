class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def display(self):
        print(f"Числа: {self.a}, {self.b}\n")
    def change(self):
        try:
            self.a = int(input("Первое число: "))
            self.b = int(input("Второе число: "))
            print("Числа изменены\n")
        except ValueError:
            print("Ошибка ввода\n")
    def sum(self):
        return self.a + self.b
    def max(self):
        return max(self.a, self.b)

def main():
    nums = Numbers(632, 122)
    while True:
        print("1. Показать")
        print("2. Изменить")
        print("3. Сумма")
        print("4. Максимум")
        print("5. Выход")
        choice = input("Выберите (1-5): ")
        if choice == "1":
            nums.display()
        elif choice == "2":
            nums.change()
        elif choice == "3":
            print(f"Сумма: {nums.sum()}\n")
        elif choice == "4":
            print(f"Максимум: {nums.max()}\n")
        elif choice == "5":
            break
if __name__ == "__main__":
    main()
