class Calculation:
    def __init__(self):
        self.calculationLine = ""
    def SetCalculationLine(self, line):
        self.calculationLine = line
    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol
    def GetCalculationLine(self):
        return self.calculationLine
    def GetLastSymbol(self):
        if len(self.calculationLine) > 0:
            return self.calculationLine[-1]
        return ""
    def DeleteLastSymbol(self):
        if len(self.calculationLine) > 0:
            self.calculationLine = self.calculationLine[:-1]

calc = Calculation()

while True:
    print("\nВыберите действие:")
    print("1. Задать строку")
    print("2. Добавить символ в конец")
    print("3. Показать текущую строку")
    print("4. Показать последний символ")
    print("5. Удалить последний символ")
    print("0. Выход")
    menu = input("Ваш выбор: ")

    if menu == "1":
        line = input("Введите строку: ")
        calc.SetCalculationLine(line)
    elif menu == "2":
        symbol = input("Введите символ: ")
        calc.SetLastSymbolCalculationLine(symbol)
    elif menu == "3":
        print("Текущая строка:", calc.GetCalculationLine())
    elif menu == "4":
        last_symbol = calc.GetLastSymbol()
        if last_symbol:
            print("Последний символ:", last_symbol)
        else:
            print("Строка пуста")
    elif menu == "5":
        calc.DeleteLastSymbol()
        print("Последний символ удален")
    elif menu == "0":
        print("Программа завершена")
        break