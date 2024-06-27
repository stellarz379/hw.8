import sqlite3

connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentor(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               ful_name VARCHAR (20)NOT NULL,
               age INT,
               email VARCHAR (30) NOT NULL,
               phone_namber VARCHAR (30)NOT NULL,
               month VARCHAR (20),
               
               coins INT 
               )""")


class GeeksMentor:
    def __init__(self):
        self.ful_name = None
        self.age = 0
        self.email = None
        self.phone_namber = None
        self.month = None
        
        self.coins = 0

    def register(self):
        ful_name = input("Введите свое имя: ")
        age = int(input("Введите свой возраст: "))
        email = input("Введите свой имейл: ")
        phone_namber = int(input("Введите свой номер: "))
        connect.commit()


    def plus_coins(self):
        id = int(input("Введите id студента:"))
        new_coins = int(input("Введите кол-во коинов:"))
        cursor.execute(f"UPDATE mentor SET coins = coins + {new_coins} WHERE id == {id}")
        self.coins += new_coins
        self.coins = self.coins + new_coins
        connect.commit()

    def minus_coins(self):
        id = int(input("Введите id студента:"))
        new_coins = int(input("Введите кол-во коинов:"))
        cursor.execute(f"UPDATE mentor SET coins = coins - {new_coins} WHERE id == {id}")
        self.coins -= new_coins
        self.coins = self.coins + new_coins
        connect.commit()

mentor = GeeksMentor()
mentor.register()
mentor.plus_coins()
mentor.minus_coins()