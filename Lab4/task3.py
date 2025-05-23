import datetime
import sqlite3
import psutil

class DataBas:
    def __init__(self, db_name="monitoring.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_db()
        self.create_table()

    def connect_db(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS monitor (
            time TEXT,
            CPU_percent REAL,
            memory_percent REAL,
            disk_percent REAL
        )""")
        self.connection.commit()

    def insert_data(self, cpu_percent, memory_percent, disk_percent):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO monitor (time, CPU_percent, memory_percent, disk_percent) VALUES (?, ?, ?, ?)",
                            (timestamp, cpu_percent, memory_percent, disk_percent))
        self.connection.commit()

    def view_all(self):
        self.cursor.execute("SELECT * FROM monitor")
        monitor = self.cursor.fetchall()
        if monitor:
            for i in monitor:
                print(i)
        else:
            print("пусто")

    def close(self):
        if self.connection:
            self.connection.close()


monitoring = DataBas()
while True:
    print("1 - Просмотреть текущее состояние")
    print("2 - Просмотреть сохранённые данные")
    print("3 - Выход")
    menu = input()

    if menu == "1":
        CPU = psutil.cpu_percent()
        print(f"Использование CPU: {CPU}%")
        RAM = psutil.virtual_memory().percent
        print(f"Использование памяти: {RAM}%")
        SSD = psutil.disk_usage('/').percent
        print(f"Использование диска: {SSD}%")
        monitoring.insert_data(CPU, RAM, SSD)
    elif menu == "2":
        monitoring.view_all()
    elif menu == "0":
        break

monitoring.close()